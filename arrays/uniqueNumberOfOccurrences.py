from typing import List
from collections import Counter


def uniqueOccurrences(arr: List[int]) -> bool:
    count = Counter(arr)
    return len(set(count.values())) == len(count.values())
