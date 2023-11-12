import unittest

from challenge_01 import challenge


class TestChallenge01(unittest.TestCase):
    def setUp(self):
        self._examples = [('gato perro perro coche Gato peRRo sol', 'gato2perro3coche1sol1'),
                          ('llaveS casa CASA casa llaves', 'llaves2casa3'),
                          ('taza ta za taza', 'taza2ta1za1'),
                          ('casas casa casasas', 'casas1casa1casasas1')]

    def test_challenge(self):
        for i, (example, result) in enumerate(self._examples):
            with self.subTest(i=i):
                self.assertEqual(challenge(example), result)


if __name__ == '__main__':
    unittest.main()
