import random


'''
Suppose an array sorted in ascending order is rotated at some pivot
unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return
its index, otherwise return -1.

You may assume no duplicate exists in the array
'''
def search_rotated_array(arr, target):
    arr.sort()
    res = False
    l, r = 0, len(arr)
    while l < r:
        mid = l + ((r + l) // 2)
        if arr[mid] < target:
            l = mid+1
        elif arr[mid] > target:
            r = mid
        else:
            res = True
    return res


if __name__ == "__main__":
    nums = [0, 1, 2, 4, 5, 6, 7]
    nums_randomized = [random.randrange(1, 10) for i in range(5)]
    print(search_rotated_array(nums_randomized, 5))
