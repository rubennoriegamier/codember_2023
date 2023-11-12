import unittest

from challenge_02 import challenge


class TestChallenge02(unittest.TestCase):
    def setUp(self):
        self._examples = [('##*&', '4'),
                          ('&##&*&@&', '0243')]

    def test_challenge(self):
        for i, (example, result) in enumerate(self._examples):
            with self.subTest(i=i):
                self.assertEqual(''.join(map(str, challenge(example))), result)


if __name__ == '__main__':
    unittest.main()
