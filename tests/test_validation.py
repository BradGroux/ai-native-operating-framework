"""Negative regressions for publication metadata and link evidence."""
import importlib.util
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('validation', ROOT / 'scripts/validate-repository.py')
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)

class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.edition = (ROOT/"VERSION").read_text().strip()
        self.released = "-".join(self.edition.split(".")[:3])
        for name in v.REQUIRED_RELEASE_FILES + ['project/planning/status.md', f'project/releases/v{self.edition}.md']:
            source = ROOT / name
            if source.is_file():
                target = self.root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
        self.patch = patch.object(v, 'REPOSITORY_ROOT', self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def check(self):
        result = v.Validation()
        v.validate_release_surface(result)
        return result.errors

    def test_current_and_complete_future_edition(self):
        self.assertEqual(self.check(), [])
        for path in self.root.rglob('*'):
            if path.is_file():
                text = path.read_text().replace(self.edition, '2028.02.29.2').replace(self.released, '2028-02-29')
                # Commons provenance is independent of product date.
                text = text.replace('/tree/v2028.02.29.2', '/tree/v2026.09.05')
                path.write_text(text)
        (self.root/f'project/releases/v{self.edition}.md').rename(self.root/'project/releases/v2028.02.29.2.md')
        self.assertEqual(self.check(), [])

    def test_cff_exact_scalar_not_prefix_or_comment(self):
        p=self.root/'CITATION.cff'; original=p.read_text()
        for value in [f'"{self.edition}.1"', f'"{self.edition}0"', f'"wrong" # version: "{self.edition}"']:
            p.write_text(original.replace(f'version: "{self.edition}"', 'version: '+value))
            self.assertTrue(self.check())
        p.write_text(original+f'\nversion: "{self.edition}"\n')
        self.assertTrue(self.check())

    def test_invalid_dates_and_missing_current_notes(self):
        p=self.root/'VERSION'
        for value in ['2026.02.30','2026.9.05','2026.09.05.0','2026.09.05.01','1.2.0']:
            p.write_text(value)
            self.assertTrue(self.check())
        p.write_text(self.edition+'\n')
        (self.root/f'project/releases/v{self.edition}.md').unlink()
        self.assertTrue(self.check())

    def test_stale_active_metadata_fails(self):
        for name in ['README.md','GOVERNANCE.md','CHANGELOG.md','project/planning/status.md','project/releases/README.md']:
            p=self.root/name;old=p.read_text();p.write_text(old.replace(self.edition,'1.1.0'))
            self.assertTrue(self.check(), name)
            p.write_text(old)

    def test_publish_runbook_stops_after_failed_preflight(self):
        import os
        import re
        runbook = (ROOT/'project/RELEASING.md').read_text()
        commands = next(block for block in re.findall(r'```sh\n(.*?)```', runbook, re.S)
                        if 'gh release create' in block)
        bindir = self.root/'bin'; bindir.mkdir()
        log = self.root/'mutations'
        stubs = {
            'gh': '#!/bin/sh\nif [ "$1" = api ]; then echo BradGroux; fi\n',
            'python3': '#!/bin/sh\nexit 1\n',
            'git': '#!/bin/sh\necho mutation >> "$MUTATION_LOG"\n',
        }
        for name, body in stubs.items():
            p=bindir/name; p.write_text(body); p.chmod(0o755)
        result = subprocess.run(['bash','-c',commands], cwd=self.root,
                                env=dict(os.environ, PATH=str(bindir)+os.pathsep+os.environ['PATH'],
                                         MUTATION_LOG=str(log)), capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(log.exists(), 'Failed preflight must not tag or push')

    def test_unpublished_link_and_fenced_heading(self):
        subprocess.run(['git','init','-q',str(self.root)],check=True)
        source=self.root/'link.md'; target=self.root/'target.md'
        source.write_text('[target](target.md#fake)\n')
        target.write_text('```md\n# Fake\n```\n# Real\n')
        subprocess.run(['git','-C',str(self.root),'add','link.md'],check=True)
        result=v.Validation();v.validate_markdown_links(result,[source])
        self.assertTrue(result.errors)
        subprocess.run(['git','-C',str(self.root),'add','target.md'],check=True)
        result=v.Validation();v.validate_markdown_links(result,[source])
        self.assertTrue(result.errors)
        source.write_text('[target](target.md#real)\n')
        result=v.Validation();v.validate_markdown_links(result,[source])
        self.assertEqual(result.errors,[])

if __name__ == '__main__':
    unittest.main()
