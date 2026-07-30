#!/usr/bin/env bash

set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
validation_temp="$(mktemp -d "${TMPDIR:-/tmp}/ai-native-framework-validation.XXXXXX")"

cleanup() {
  find "$validation_temp" -depth -delete
}
trap cleanup EXIT

if [[ $# -ne 0 ]]; then
  echo "Usage: scripts/validate-repository.sh" >&2
  exit 2
fi

cd "$repository_root"

for required_command in curl git npx python3 ruby tar; do
  if ! command -v "$required_command" >/dev/null 2>&1; then
    echo "Required validation command is unavailable: $required_command" >&2
    exit 1
  fi
done

download_verified_binary() {
  local url="$1"
  local expected_checksum="$2"
  local binary_name="$3"
  local destination_directory="$4"
  local archive="$destination_directory/archive.tar.gz"
  local actual_checksum

  mkdir -p "$destination_directory"
  curl --fail --location --silent --show-error --output "$archive" "$url"
  actual_checksum="$(
    python3 -c \
      'import hashlib, pathlib, sys; print(hashlib.sha256(pathlib.Path(sys.argv[1]).read_bytes()).hexdigest())' \
      "$archive"
  )"
  if [[ "$actual_checksum" != "$expected_checksum" ]]; then
    echo "Checksum mismatch for $url" >&2
    exit 1
  fi
  tar --extract --gzip --file "$archive" --directory "$destination_directory" "$binary_name"
  printf '%s/%s\n' "$destination_directory" "$binary_name"
}

kernel_name="$(uname -s)"
machine_name="$(uname -m)"
case "$kernel_name/$machine_name" in
  Darwin/arm64)
    actionlint_archive="actionlint_1.7.12_darwin_arm64.tar.gz"
    actionlint_checksum="aba9ced2dee8d27fecca3dc7feb1a7f9a52caefa1eb46f3271ea66b6e0e6953f"
    gitleaks_archive="gitleaks_8.30.1_darwin_arm64.tar.gz"
    gitleaks_checksum="b40ab0ae55c505963e365f271a8d3846efbc170aa17f2607f13df610a9aeb6a5"
    ;;
  Darwin/x86_64)
    actionlint_archive="actionlint_1.7.12_darwin_amd64.tar.gz"
    actionlint_checksum="5b44c3bc2255115c9b69e30efc0fecdf498fdb63c5d58e17084fd5f16324c644"
    gitleaks_archive="gitleaks_8.30.1_darwin_x64.tar.gz"
    gitleaks_checksum="dfe101a4db2255fc85120ac7f3d25e4342c3c20cf749f2c20a18081af1952709"
    ;;
  Linux/x86_64)
    actionlint_archive="actionlint_1.7.12_linux_amd64.tar.gz"
    actionlint_checksum="8aca8db96f1b94770f1b0d72b6dddcb1ebb8123cb3712530b08cc387b349a3d8"
    gitleaks_archive="gitleaks_8.30.1_linux_x64.tar.gz"
    gitleaks_checksum="551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb"
    ;;
  Linux/aarch64)
    actionlint_archive="actionlint_1.7.12_linux_arm64.tar.gz"
    actionlint_checksum="325e971b6ba9bfa504672e29be93c24981eeb1c07576d730e9f7c8805afff0c6"
    gitleaks_archive="gitleaks_8.30.1_linux_arm64.tar.gz"
    gitleaks_checksum="e4a487ee7ccd7d3a7f7ec08657610aa3606637dab924210b3aee62570fb4b080"
    ;;
  *)
    echo "Unsupported validation platform: $kernel_name/$machine_name" >&2
    exit 1
    ;;
esac

if command -v actionlint >/dev/null 2>&1; then
  actionlint_command="$(command -v actionlint)"
else
  actionlint_command="$(
    download_verified_binary \
      "https://github.com/rhysd/actionlint/releases/download/v1.7.12/$actionlint_archive" \
      "$actionlint_checksum" \
      actionlint \
      "$validation_temp/actionlint"
  )"
fi

if command -v gitleaks >/dev/null 2>&1; then
  gitleaks_command="$(command -v gitleaks)"
else
  gitleaks_command="$(
    download_verified_binary \
      "https://github.com/gitleaks/gitleaks/releases/download/v8.30.1/$gitleaks_archive" \
      "$gitleaks_checksum" \
      gitleaks \
      "$validation_temp/gitleaks"
  )"
fi

mermaid_input="$validation_temp/mermaid-diagrams.md"
mermaid_output="$validation_temp/rendered-diagrams.md"
mermaid_assets="$validation_temp/rendered-assets"

python3 scripts/validate-repository.py --mermaid-document "$mermaid_input"

yaml_files=(CITATION.cff)
while IFS= read -r -d '' yaml_file; do
  yaml_files+=("$yaml_file")
done < <(find .github -type f \( -name '*.yml' -o -name '*.yaml' \) -print0)

ruby -e \
  'require "yaml"; ARGV.each { |file| Psych.parse_file(file); puts "PASS: YAML syntax: #{file}" }' \
  "${yaml_files[@]}"

"$actionlint_command" .github/workflows/validate-release.yml
echo "PASS: GitHub Actions semantic validation"

if command -v cffconvert >/dev/null 2>&1; then
  cffconvert --validate
elif command -v uvx >/dev/null 2>&1; then
  uvx --from cffconvert==2.0.0 cffconvert --validate
else
  python3 -m venv "$validation_temp/cff-environment"
  "$validation_temp/cff-environment/bin/python" -m pip \
    --disable-pip-version-check --quiet install cffconvert==2.0.0
  "$validation_temp/cff-environment/bin/cffconvert" --validate
fi
echo "PASS: CFF 1.2 metadata validation"

mkdir -p "$mermaid_assets"
mermaid_arguments=(
  --input "$mermaid_input"
  --output "$mermaid_output"
  --artefacts "$mermaid_assets"
  --quiet
)
if [[ "${CI:-}" == "true" && "$kernel_name" == "Linux" ]]; then
  mermaid_arguments+=(
    --puppeteerConfigFile scripts/puppeteer-ci-config.json
  )
fi
npx --yes @mermaid-js/mermaid-cli@11.16.0 "${mermaid_arguments[@]}"

expected_diagrams="$(grep -c '^```mermaid$' "$mermaid_input")"
rendered_diagrams="$(find "$mermaid_assets" -type f -name '*.svg' | wc -l | tr -d ' ')"
if [[ "$expected_diagrams" != "$rendered_diagrams" ]]; then
  echo "Mermaid render mismatch: expected $expected_diagrams, rendered $rendered_diagrams" >&2
  exit 1
fi
echo "PASS: Mermaid rendering: $rendered_diagrams diagrams"

"$gitleaks_command" dir . --no-banner --redact
"$gitleaks_command" git . --no-banner --redact
echo "PASS: Gitleaks working-tree and Git-history scans"

echo "All repository validation checks passed."
