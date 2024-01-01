from dp.wordBreak import wordBreak
import unittest


class DpUnitTests(unittest.TestCase):
    def test_wordBreak(self):
        test_inputs = [
            ['leetcode', ['leet', 'code']],
            ['applepenapple', ['apple', 'pen']],
            ['catsandogs', ["cats", "dog", "sand", "and", "cat"]],
            ['programmingisfun', ['programming', 'is', 'fun']],
            ['abcd', ['ab', 'cd', 'abc', 'd']],
            ['', []],
            ['abcd', []],
            ['aaaaaaa', ['a', 'aa', 'aaa']],

        ]
        solutions = [True, True, False, True, True, True, False, True]
        for i in range(len(test_inputs)):
            s, wordDict = test_inputs[i]
            self.assertEqual(
                wordBreak(s, wordDict),
                solutions[i],
                f'Incorrect Output. Expected: {solutions[i]}')


if __name__ == '__main__':
    unittest.main()
