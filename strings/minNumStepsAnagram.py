from collections import Counter


def minSteps(s, t):
    sCount = Counter(s)
    tCount = Counter(t)
    res = 0
    for char in sCount:
        subbed = sCount.get(char, 0) - tCount.get(char, 0)
        if subbed > 0:
            res += subbed
    return res
