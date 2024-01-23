from collections import Counter


def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    charSet1 = set()
    charSet2 = set()
    charFreq1, charFreq2 = [0] * 26, [0] * 26
    for i in range(len(word1)):
        charSet1.add(word1[i])
        charSet2.add(word2[i])
        charFreq1[ord(word1[i]) - ord('a')] += 1
        charFreq2[ord(word2[i]) - ord('a')] += 1
    charFreq1.sort()
    charFreq2.sort()

    return charSet1 == charSet2 and charFreq1 == charFreq2
