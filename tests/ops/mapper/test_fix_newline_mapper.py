import unittest

from data_juicer.ops.mapper.fix_newline_mapper import FixNewlineMapper


class FixNewlineMapperTest(unittest.TestCase):

    def setUp(self):
        self.op = FixNewlineMapper()

    def _run_fix_newline(self, samples):
        for sample in samples:
            result = self.op.process(sample)
            self.assertEqual(result['text'], result['target'])

    def test_good_newline_text(self):
        samples = [
            {
                'text': 'foo\n',
                'target': 'foo\n',
            },
            {
                'text': 'foo\nbar',
                'target': 'foo\nbar',
            },
            {
                'text': 'foo\nbar\nbaz',
                'target': 'foo\nbar\nbaz',
            },
        ]
        self._run_fix_newline(samples)

    def test_bad_newline_text(self):
        samples = [
            {
                'text': 'foo\\n',
                'target': 'foo\n',
            },
            {
                'text': 'foo\\nbar',
                'target': 'foo\nbar',
            },
            {
                'text': 'foo\\nbar\\nbaz',
                'target': 'foo\nbar\nbaz',
            },
        ]
        self._run_fix_newline(samples)

    def test_no_newline_text(self):
        samples = [
            {
                'text': '',
                'target': '',
            },
            {
                'text': 'foo',
                'target': 'foo',
            },
        ]
        self._run_fix_newline(samples)


if __name__ == '__main__':
    unittest.main()
