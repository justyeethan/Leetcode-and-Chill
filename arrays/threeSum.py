from typing import List


def threeSum(nums: List[int]) -> List[int]:
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            subbed = nums[i] + nums[lo] + nums[hi]
            if subbed > 0:
                hi -= 1
            elif subbed < 0:
                lo += 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                while nums[lo] == nums[lo-1] and lo < hi:
                    lo += 1

    return res
