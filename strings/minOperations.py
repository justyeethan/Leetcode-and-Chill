def minOperations(s: str) -> int:
    res = 0
    for i in range(len(s)):
        if i % 2:
            res += 1 if s[i] == '0' else 0
        else:
            res += 1 if s[i] == '1' else 0
    return min(res, len(s)-res)