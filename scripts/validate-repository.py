#!/usr/bin/env python3
"""Validate the repository's documentation and framework invariants."""

from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRECTORIES = {".git", ".venv", "node_modules"}

EXPECTED_CONCERNS = [
    "Intent",
    "Responsibility",
    "Work",
    "Control",
    "Assurance",
    "Learning",
]

EXPECTED_SOP_REQUIREMENTS = [
    "Purpose, Scope, and Expected Outcome",
    "Ownership, Participation, Responsibility, and Authority",
    "Trigger, Prerequisites, Inputs, and Authoritative Sources",
    "Activities, Decisions, Dependencies, Handoffs, and Outputs",
    "Policies, Controls, Approvals, and Risks",
    "Exceptions, Escalation, Recovery, and Stop Conditions",
    "Completion, Verification, Quality, and Evidence",
    "Review Ownership, Review Triggers, and Change History",
]

EXPECTED_MAINTENANCE_ACTIVITIES = [
    "Understand",
    "Document",
    "Validate",
    "Approve",
    "Use",
    "Improve",
]

EXPECTED_EXAMPLE_NUMBERS = [f"{number:02d}" for number in range(1, 12)]

ALLOWED_NUMBERED_EXAMPLE_HEADINGS = [
    {"Purpose, Scope, and Expected Outcome"},
    {
        "Roles, Responsibilities, and Authority",
        "Ownership, Participation, Responsibility, and Authority",
    },
    {"Trigger, Prerequisites, Inputs, and Authoritative Sources"},
    {
        "Procedure",
        "Activities, Decisions, Dependencies, Handoffs, and Outputs",
    },
    {"Policies, Controls, Approvals, and Risks"},
    {"Exceptions, Escalation, Recovery, and Stop Conditions"},
    {
        "Completion, Verification, and Evidence",
        "Completion, Verification, Quality, and Evidence",
    },
    {
        "Review, Approval, and Change History",
        "Review Ownership, Review Triggers, and Change History",
    },
]

REQUIRED_EXAMPLE_LABELS = [
    "## Example Record",
    "## Scenario Overview",
    "# SOP:",
    "**Provenance:**",
    "**Review status:**",
    "**Draft contributor:**",
    "**Responsible maintainer:**",
    "**Publication-safety note:**",
    "**Review triggers:**",
    "## Framework Annotation",
    "## Domain-Specific Boundary",
    "## Related Framework Documents",
]

TRACEABILITY_ROW_PREFIXES = [
    "Purpose, scope, and expected outcome",
    "Ownership, participation, responsibility, and authority",
    "Trigger, prerequisites, inputs, and authoritative sources",
    "Activities, decisions, dependencies, handoffs, and outputs",
    "Policies, controls, approvals, and risks",
    "Exceptions, escalation, recovery, and stop conditions",
    "Completion, verification, quality, and evidence",
    "Review ownership, review triggers, and change history",
]

REQUIRED_RELEASE_FILES = [
    ".github/CODEOWNERS",
    ".github/ISSUE_TEMPLATE/appeal.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/framework-contribution.yml",
    ".github/ISSUE_TEMPLATE/private-conduct-contact.yml",
    ".github/ISSUE_TEMPLATE/private-sensitive-disclosure-contact.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/validate-release.yml",
    "AGENTS.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "LICENSE.md",
    "README.md",
    "SECURITY.md",
    "scripts/puppeteer-ci-config.json",
    "scripts/validate-repository.py",
    "scripts/validate-repository.sh",
]

MARKDOWN_LINK_PATTERN = re.compile(
    r"!?\[[^\]]*\]\(([^)\n]+)\)",
    flags=re.MULTILINE,
)
REFERENCE_LINK_PATTERN = re.compile(
    r"^\[[^\]]+\]:\s*(\S+)",
    flags=re.MULTILINE,
)
FENCED_BLOCK_PATTERN = re.compile(
    r"^```[^\n]*\n.*?^```[ \t]*$",
    flags=re.MULTILINE | re.DOTALL,
)
MERMAID_BLOCK_PATTERN = re.compile(
    r"^```mermaid[ \t]*\n(.*?)^```[ \t]*$",
    flags=re.MULTILINE | re.DOTALL,
)
EMAIL_PATTERN = re.compile(
    r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
    flags=re.IGNORECASE,
)
ALLOWED_PUBLIC_COMMIT_IDENTIFIERS = {
    # actions/checkout v6
    "d23441a48e516b6c34aea4fa41551a30e30af803",
    # actions/setup-python v7
    "5fda3b95a4ea91299a34e894583c3862153e4b97",
}


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.results: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)

    def pass_result(self, message: str) -> None:
        self.results.append(message)


def repository_files(suffix: str | None = None) -> list[Path]:
    files: list[Path] = []
    for candidate in REPOSITORY_ROOT.rglob("*"):
        if not candidate.is_file():
            continue
        if any(part in EXCLUDED_DIRECTORIES for part in candidate.parts):
            continue
        if suffix is not None and candidate.suffix.lower() != suffix:
            continue
        files.append(candidate)
    return sorted(files)


def git_publication_text_files() -> list[Path]:
    result = subprocess.run(
        [
            "git",
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
            "-z",
        ],
        cwd=REPOSITORY_ROOT,
        check=True,
        capture_output=True,
    )
    text_files: list[Path] = []
    for raw_path in result.stdout.split(b"\0"):
        if not raw_path:
            continue
        candidate = REPOSITORY_ROOT / raw_path.decode("utf-8")
        if not candidate.is_file():
            continue
        try:
            candidate.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        text_files.append(candidate)
    return sorted(text_files)


def relative(path: Path) -> str:
    return path.relative_to(REPOSITORY_ROOT).as_posix()


def without_fenced_blocks(text: str) -> str:
    return FENCED_BLOCK_PATTERN.sub("", text)


def link_destination(raw_destination: str) -> str:
    destination = raw_destination.strip()
    if destination.startswith("<") and ">" in destination:
        return destination[1 : destination.index(">")]
    return destination.split(maxsplit=1)[0]


def github_heading_anchors(markdown_path: Path) -> set[str]:
    text = markdown_path.read_text(encoding="utf-8")
    anchors: set[str] = set()
    duplicate_counts: dict[str, int] = {}

    for heading_match in re.finditer(
        r"^#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$",
        text,
        flags=re.MULTILINE,
    ):
        heading = heading_match.group(1)
        heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading)
        heading = re.sub(r"<[^>]+>", "", heading)
        heading = html.unescape(heading)
        heading = re.sub(r"[`*_~]", "", heading)
        heading = "".join(
            character
            for character in heading.lower()
            if character.isalnum() or character in {" ", "-", "_"}
        )
        slug = re.sub(r"\s", "-", heading)
        if not slug:
            continue

        duplicate_number = duplicate_counts.get(slug, 0)
        duplicate_counts[slug] = duplicate_number + 1
        if duplicate_number:
            slug = f"{slug}-{duplicate_number}"
        anchors.add(slug)

    for anchor_match in re.finditer(
        r"<a\s+(?:id|name)=[\"']([^\"']+)[\"']",
        text,
        flags=re.IGNORECASE,
    ):
        anchors.add(anchor_match.group(1))

    return anchors


def validate_markdown_links(validation: Validation, markdown_files: list[Path]) -> None:
    anchor_cache: dict[Path, set[str]] = {}
    local_reference_count = 0

    for markdown_path in markdown_files:
        text = markdown_path.read_text(encoding="utf-8")
        searchable_text = without_fenced_blocks(text)
        destinations = list(MARKDOWN_LINK_PATTERN.finditer(searchable_text))
        destinations.extend(REFERENCE_LINK_PATTERN.finditer(searchable_text))

        for match in destinations:
            destination = link_destination(match.group(1))
            if (
                not destination
                or destination.startswith("//")
                or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", destination)
            ):
                continue

            line_number = searchable_text.count("\n", 0, match.start()) + 1
            decoded_destination = unquote(destination)
            path_part, separator, fragment = decoded_destination.partition("#")
            path_part = path_part.partition("?")[0]

            if path_part.startswith("/"):
                validation.errors.append(
                    f"{relative(markdown_path)}:{line_number}: "
                    f"repository-local link must be relative: {destination}"
                )
                continue

            target_path = (
                markdown_path
                if not path_part
                else (markdown_path.parent / path_part).resolve()
            )
            local_reference_count += 1

            try:
                target_path.relative_to(REPOSITORY_ROOT)
            except ValueError:
                validation.errors.append(
                    f"{relative(markdown_path)}:{line_number}: "
                    f"link escapes the repository: {destination}"
                )
                continue

            if not target_path.exists():
                validation.errors.append(
                    f"{relative(markdown_path)}:{line_number}: "
                    f"missing local link target: {destination}"
                )
                continue

            if separator and fragment and target_path.suffix.lower() == ".md":
                if target_path not in anchor_cache:
                    anchor_cache[target_path] = github_heading_anchors(target_path)
                normalized_fragment = fragment.lower()
                if normalized_fragment not in anchor_cache[target_path]:
                    validation.errors.append(
                        f"{relative(markdown_path)}:{line_number}: "
                        f"missing heading #{fragment} in {relative(target_path)}"
                    )

    validation.pass_result(
        f"Markdown links: {len(markdown_files)} documents and "
        f"{local_reference_count} local references checked"
    )


def numbered_headings(
    path: Path,
    heading_level: int,
    count: int,
    separator: str,
) -> list[str]:
    text = path.read_text(encoding="utf-8")
    marker = "#" * heading_level
    pattern = rf"^{marker} ([1-{count}]){re.escape(separator)} (.+)$"
    matches = re.findall(pattern, text, flags=re.MULTILINE)
    return [heading for _, heading in sorted(matches, key=lambda item: int(item[0]))]


def validate_canonical_vocabulary(validation: Validation) -> None:
    concerns = numbered_headings(
        REPOSITORY_ROOT / "framework/operating-framework.md",
        heading_level=3,
        count=6,
        separator=".",
    )
    validation.require(
        concerns == EXPECTED_CONCERNS,
        f"framework/operating-framework.md: expected concerns "
        f"{EXPECTED_CONCERNS}, found {concerns}",
    )

    sop_requirements = numbered_headings(
        REPOSITORY_ROOT / "framework/sop-content-standard.md",
        heading_level=3,
        count=8,
        separator=".",
    )
    validation.require(
        sop_requirements == EXPECTED_SOP_REQUIREMENTS,
        "framework/sop-content-standard.md: the eight SOP content "
        f"requirements changed: {sop_requirements}",
    )

    maintenance_path = REPOSITORY_ROOT / "framework/standards-maintenance-method.md"
    maintenance_text = maintenance_path.read_text(encoding="utf-8")
    activities = [
        activity
        for _, activity in sorted(
            re.findall(
                r"^## Activity ([1-6]) — (.+)$",
                maintenance_text,
                flags=re.MULTILINE,
            ),
            key=lambda item: int(item[0]),
        )
    ]
    validation.require(
        activities == EXPECTED_MAINTENANCE_ACTIVITIES,
        "framework/standards-maintenance-method.md: the six maintenance "
        f"activities changed: {activities}",
    )

    validation.pass_result(
        "Canonical vocabulary: 6 concerns, 8 SOP requirements, and "
        "6 maintenance activities checked"
    )


def validate_examples(validation: Validation) -> None:
    examples = sorted((REPOSITORY_ROOT / "examples").glob("[0-9][0-9]-*.md"))
    example_numbers = [path.name[:2] for path in examples]
    validation.require(
        example_numbers == EXPECTED_EXAMPLE_NUMBERS,
        f"examples/: expected examples 01 through 11, found {example_numbers}",
    )

    for example_path in examples:
        text = example_path.read_text(encoding="utf-8")
        name = relative(example_path)

        for label in REQUIRED_EXAMPLE_LABELS:
            validation.require(
                label in text,
                f"{name}: missing required example element: {label}",
            )

        for concern in EXPECTED_CONCERNS:
            concern_rows = re.findall(
                rf"^\|\s*{re.escape(concern)}\s*\|",
                text,
                flags=re.MULTILINE,
            )
            validation.require(
                len(concern_rows) == 1,
                f"{name}: expected one Framework Annotation row for "
                f"{concern}, found {len(concern_rows)}",
            )

        numbered_headings_found = re.findall(
            r"^## ([1-8])\. (.+)$",
            text,
            flags=re.MULTILINE,
        )
        numbered_sections = {number for number, _ in numbered_headings_found}
        if numbered_sections == set("12345678"):
            ordered_headings = [
                heading
                for _, heading in sorted(
                    numbered_headings_found,
                    key=lambda item: int(item[0]),
                )
            ]
            for section_index, allowed_headings in enumerate(
                ALLOWED_NUMBERED_EXAMPLE_HEADINGS,
                start=1,
            ):
                validation.require(
                    ordered_headings[section_index - 1] in allowed_headings,
                    f"{name}: section {section_index} does not communicate the "
                    "expected SOP content area",
                )
        else:
            validation.require(
                "### SOP Content Traceability" in text,
                f"{name}: does not have sections 1 through 8 or an SOP "
                "Content Traceability table",
            )
            for row_prefix in TRACEABILITY_ROW_PREFIXES:
                validation.require(
                    re.search(
                        rf"^\|\s*{re.escape(row_prefix)}\s*\|",
                        text,
                        flags=re.MULTILINE | re.IGNORECASE,
                    )
                    is not None,
                    f"{name}: missing SOP traceability row: {row_prefix}",
                )

    validation.pass_result(
        f"Examples: {len(examples)} examples checked across 8 SOP content "
        "areas and 6 concerns"
    )


def validate_operating_memory(validation: Validation) -> None:
    memory_path = REPOSITORY_ROOT / "framework/shared-operating-memory-standard.md"
    memory_text = memory_path.read_text(encoding="utf-8")
    normalized_memory_text = re.sub(
        r"\s+",
        " ",
        re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", memory_text),
    ).lower()
    exact_invariants = [
        (
            "shared operating memory connects four existing framework concerns. "
            "it is not a seventh concern."
        ),
        ("the eight requirements in the sop content standard also remain unchanged."),
        "storage does not create authority.",
        (
            "the responsible human owner remains accountable for business "
            "authority, control, and approval."
        ),
    ]
    for invariant in exact_invariants:
        validation.require(
            invariant in normalized_memory_text,
            f"{relative(memory_path)}: missing exact operating-memory "
            f"invariant: {invariant}",
        )

    required_headings = [
        "## Memory Authority",
        "## Handoff Standard",
        "## Provenance, Confidence, and Uncertainty",
        "## Access, Privacy, Security, Rights, and Retention",
        "## Verification, Conflict, and Correction",
        "## Supersession, Retention, and Disposal",
        "## Resilience and Recovery",
    ]
    for heading in required_headings:
        validation.require(
            heading in memory_text,
            f"{relative(memory_path)}: missing operating-memory safeguard "
            f"section: {heading}",
        )

    validation.require(
        "The framework does not require:" in memory_text
        and "- or a machine-specific schema or representation." in memory_text,
        f"{relative(memory_path)}: technology independence boundary changed",
    )
    validation.require(
        "- technology migration;" in memory_text,
        f"{relative(memory_path)}: technology-migration recovery check changed",
    )

    validation.pass_result(
        "Shared operating memory: authority, provenance, handoff, privacy, "
        "retention, correction, recovery, and technology independence checked"
    )


def validate_release_surface(validation: Validation) -> None:
    for required_file in REQUIRED_RELEASE_FILES:
        validation.require(
            (REPOSITORY_ROOT / required_file).is_file(),
            f"missing required release file: {required_file}",
        )

    citation_text = (REPOSITORY_ROOT / "CITATION.cff").read_text(encoding="utf-8")
    citation_requirements = [
        "cff-version: 1.2.0",
        "license: MIT",
        "version: 1.0.0",
        "date-released: 2026-07-30",
        "https://github.com/bradgroux/ai-native-operating-framework",
    ]
    for requirement in citation_requirements:
        validation.require(
            requirement in citation_text,
            f"CITATION.cff: missing release metadata: {requirement}",
        )

    workflow_path = REPOSITORY_ROOT / ".github/workflows/validate-release.yml"
    if workflow_path.is_file():
        workflow_text = workflow_path.read_text(encoding="utf-8")
        action_uses = re.findall(
            r"^\s*uses:\s*[^@\s]+@(\S+)",
            workflow_text,
            re.MULTILINE,
        )
        for action_reference in action_uses:
            validation.require(
                re.fullmatch(r"[0-9a-f]{40}", action_reference) is not None,
                ".github/workflows/validate-release.yml: external actions "
                f"must use a full commit identifier, found {action_reference}",
            )

    validation.pass_result(
        f"Release surface: {len(REQUIRED_RELEASE_FILES)} required files and "
        "version 1.0.0 metadata checked"
    )


def validate_publication_safety(
    validation: Validation,
) -> None:
    patterns = [
        (
            "absolute local user path",
            re.compile(r"/(?:Users|home)/[A-Za-z0-9._-]+(?:/|\b)"),
        ),
        ("local file URI", re.compile("file:" + "//", flags=re.IGNORECASE)),
        (
            "private platform path",
            re.compile(r"(?:^|[/\s])\.buzz(?:[/\s]|$)", flags=re.IGNORECASE),
        ),
        (
            "private cloud filesystem marker",
            re.compile(r"Mobile\s+Documents", flags=re.IGNORECASE),
        ),
        (
            "full internal commit identifier",
            re.compile(r"\b[0-9a-f]{40}\b", flags=re.IGNORECASE),
        ),
        (
            "UUID-like private identifier",
            re.compile(
                r"\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-"
                r"[89ab][0-9a-f]{3}-[0-9a-f]{12}\b",
                flags=re.IGNORECASE,
            ),
        ),
    ]

    publication_files = git_publication_text_files()
    for publication_path in publication_files:
        text = publication_path.read_text(encoding="utf-8")
        for description, pattern in patterns:
            for finding in pattern.finditer(text):
                if (
                    description == "full internal commit identifier"
                    and finding.group(0).lower() in ALLOWED_PUBLIC_COMMIT_IDENTIFIERS
                ):
                    continue
                line_number = text.count("\n", 0, finding.start()) + 1
                validation.errors.append(
                    f"{relative(publication_path)}:{line_number}: "
                    f"possible {description}"
                )

        for email_match in EMAIL_PATTERN.finditer(text):
            email = email_match.group(0).lower()
            if email.endswith("@users.noreply.github.com"):
                continue
            if email.rsplit("@", maxsplit=1)[1] in {
                "example.com",
                "example.net",
                "example.org",
            }:
                continue
            line_number = text.count("\n", 0, email_match.start()) + 1
            validation.errors.append(
                f"{relative(publication_path)}:{line_number}: "
                "possible personal email address"
            )

    validation.pass_result(
        f"Publication safety: {len(publication_files)} Git-listed UTF-8 files "
        "checked for private identifiers"
    )


def extract_mermaid(
    validation: Validation,
    markdown_files: list[Path],
    output_path: Path | None,
) -> int:
    diagrams: list[tuple[Path, int, str]] = []

    for markdown_path in markdown_files:
        text = markdown_path.read_text(encoding="utf-8")
        opening_count = len(re.findall(r"^```mermaid[ \t]*$", text, flags=re.MULTILINE))
        blocks = MERMAID_BLOCK_PATTERN.findall(text)
        validation.require(
            opening_count == len(blocks),
            f"{relative(markdown_path)}: found {opening_count} Mermaid openings "
            f"but {len(blocks)} complete blocks",
        )
        diagrams.extend(
            (markdown_path, index, block.strip())
            for index, block in enumerate(blocks, start=1)
        )

    validation.require(
        len(diagrams) >= 26,
        f"expected at least 26 Mermaid diagrams, found {len(diagrams)}",
    )

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_lines = [
            "# Extracted Mermaid Diagrams",
            "",
            "Generated temporarily by the repository validation command.",
            "",
        ]
        for sequence, (source_path, source_index, diagram) in enumerate(
            diagrams,
            start=1,
        ):
            output_lines.extend(
                [
                    (
                        f"## Diagram {sequence}: {relative(source_path)} "
                        f"block {source_index}"
                    ),
                    "",
                    "```mermaid",
                    diagram,
                    "```",
                    "",
                ]
            )
        output_path.write_text("\n".join(output_lines), encoding="utf-8")

    validation.pass_result(f"Mermaid structure: {len(diagrams)} diagrams extracted")
    return len(diagrams)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate links, vocabulary, examples, memory safeguards, "
        "release metadata, publication safety, and Mermaid structure."
    )
    parser.add_argument(
        "--mermaid-document",
        type=Path,
        help="write all Mermaid blocks to a temporary Markdown document",
    )
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    validation = Validation()
    markdown_files = repository_files(".md")

    validate_markdown_links(validation, markdown_files)
    validate_canonical_vocabulary(validation)
    validate_examples(validation)
    validate_operating_memory(validation)
    validate_release_surface(validation)
    validate_publication_safety(validation)
    diagram_count = extract_mermaid(
        validation,
        markdown_files,
        arguments.mermaid_document,
    )

    if validation.errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in validation.errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    for result in validation.results:
        print(f"PASS: {result}")
    print(
        f"Repository validation passed: {len(markdown_files)} Markdown "
        f"documents and {diagram_count} Mermaid diagrams."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
