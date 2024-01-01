
def maxLengthBetweenEqualCharacters(s: str) -> int:
    """
    https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/?envType=daily-question&envId=2023-12-31
    """
    maxLength = -1
    seen = {}  # hold the value with the index
    for i in range(len(s)):
        if s[i] in seen:
            maxLength = max(i - seen[s[i]] - 1, maxLength)
            seen[s[i]] = i  # Update the pointer
            # Consider this: abcajklsowea, would it update again?
        else:
            seen[s[i]] = i
    return maxLength
