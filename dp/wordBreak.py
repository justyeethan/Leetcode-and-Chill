from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    """
    https://leetcode.com/problems/word-break/description/?envType=daily-question&envId=2023-12-31
    Needs a DP approach since we need to remember the values
    See this example where wordDict has substrings:
    wordDict = ['aa', 'aaa']
    s = 'aaaaa'

    It would only match duplicates with aa and return false
    when there's a left-over, so we need some sort of dp implementation
    """
    dp = [True] + [False] * (len(s))
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1] in wordDict:
                dp[j+1] = dp[i] or dp[j+1]
    return dp[-1]
