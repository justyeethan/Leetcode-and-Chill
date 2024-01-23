import unittest

# String imports
from strings.maxLengthBetweenCharacters import maxLengthBetweenEqualCharacters
from strings.minNumStepsAnagram import minSteps
from strings.closeStrings import closeStrings


class StringUnitTests(unittest.TestCase):
    def test_maxLengthBetweenEqualCharacters(self):
        tests = ["aa", 'abca', 'cbzxy']
        solutions = [0, 2, -1]
        for i, t in enumerate(tests):
            self.assertEqual(
                maxLengthBetweenEqualCharacters(t),
                solutions[i],
                f'Incorrect Output. Expected: {solutions[i]}')

    def test_minSteps(self):
        tests = [['bab', 'aba'], ['leetcode',
                                  'practice'], ['anagram', 'mangaar']]
        solutions = [1, 5, 0]
        for i, t in enumerate(tests):
            self.assertEqual(
                minSteps(t[0], t[1]),
                solutions[i],
                f'Incorrect Output. Expected: {solutions[i]}')

    def test_closeStrings(self):
        tests = [['abc', 'bca'], ['a', 'aa'], ['cabbba', 'abbccc']]
        solutions = [True, False, True]
        for i, t in enumerate(tests):
            self.assertEqual(
                closeStrings(t[0], t[1]),
                solutions[i],
                f'Incorrect Output. Expected: {solutions[i]}')


if __name__ == '__main__':
    unittest.main()
