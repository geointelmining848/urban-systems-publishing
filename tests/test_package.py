"""Portable package invariants; these tests do not measure model behavior."""
from pathlib import Path
import json
import re
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'urban-systems-publishing'


class PackageTests(unittest.TestCase):
    def test_skill_metadata_and_routing(self):
        text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        front = yaml.safe_load(text.split('---', 2)[1])
        self.assertEqual(front['name'], SKILL.name)
        self.assertTrue(0 < len(front['description']) <= 1024)
        ui = yaml.safe_load((SKILL / 'agents/openai.yaml').read_text(encoding='utf-8'))
        self.assertIn('$' + SKILL.name, ui['interface']['default_prompt'])
        self.assertTrue(25 <= len(ui['interface']['short_description']) <= 64)
        for reference in (SKILL / 'references').glob('*.md'):
            self.assertIn('references/' + reference.name, text, reference.name)

    def test_relative_markdown_links_resolve(self):
        for path in ROOT.rglob('*.md'):
            if any(part.startswith('.') for part in path.relative_to(ROOT).parts):
                continue
            for raw in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                target = raw.split('#', 1)[0]
                if not target or re.match(r'^[a-z]+:', target):
                    continue
                target = target.strip('<>')
                self.assertTrue((path.parent / target).exists(), f'{path.relative_to(ROOT)} -> {target}')

    def test_scenarios_are_distinct_and_include_boundaries(self):
        data = json.loads((SKILL / 'evals/evals.json').read_text(encoding='utf-8'))
        cases = data['evals']
        self.assertEqual(len({x['id'] for x in cases}), len(cases))
        self.assertEqual(len({x['prompt'] for x in cases}), len(cases))
        self.assertEqual({'positive', 'negative', 'edge'}, {x['category'] for x in cases})
        self.assertTrue(any(re.search(r'[\u4e00-\u9fff]', x['prompt']) for x in cases))
        for case in cases:
            self.assertTrue(case['assertions'] and case['failure_condition'])
            self.assertIsInstance(case['should_trigger'], bool)
            self.assertEqual(case['files'], [])  # cases require no private artifacts

    def test_public_text_has_no_account_paths_or_secret_material(self):
        patterns = [r'[A-Za-z]:[\\/]Users[\\/][\w.-]+', r'/home/[\w.-]+/',
                    r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                    r'gh[pousr]_[A-Za-z0-9]{20,}', r'github_pat_[A-Za-z0-9_]{20,}']
        for path in ROOT.rglob('*'):
            if not path.is_file() or '.git' in path.parts or '__pycache__' in path.parts:
                continue
            if path.suffix not in {'.md', '.py', '.json', '.txt', '.yaml', '.yml'}:
                continue
            text = path.read_text(encoding='utf-8')
            self.assertNotIn('\ufffd', text, str(path))
            for pattern in patterns:
                self.assertIsNone(re.search(pattern, text), f'{path.relative_to(ROOT)}: sensitive pattern')
        self.assertFalse(any(ROOT.rglob('*.parquet')))
        self.assertFalse(any(ROOT.rglob('*.jsonl')))


if __name__ == '__main__':
    unittest.main()
