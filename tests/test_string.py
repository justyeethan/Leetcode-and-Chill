import unittest

# String imports
from strings.maxLengthBetweenCharacters import maxLengthBetweenEqualCharacters


class StringUnitTests(unittest.TestCase):
    def test_maxLengthBetweenEqualCharacters(self):
        tests = ["aa", 'abca', 'cbzxy']
        solutions = [0, 2, -1]
        for i, t in enumerate(tests):
            self.assertEqual(
                maxLengthBetweenEqualCharacters(t),
                solutions[i],
                f'Incorrect Output. Expected: {solutions[i]}')


if __name__ == '__main__':
    unittest.main()
