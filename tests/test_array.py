from components.ListNode import ListNode

# Array imports
from arrays.fourSum import four_sum
from arrays.containsDuplicate import containsDuplicate
from arrays.searchRotatedArray import searchRotatedArray
from arrays.mergeSortedArray import mergeSortedArray
from arrays.threeSum import threeSum
from arrays.assignCookies import findContentChildren
from arrays.uniqueNumberOfOccurrences import uniqueOccurrences


import unittest


class ArrayUnitTests(unittest.TestCase):
    def test_assignCookies(self):
        self.assertEqual(
            findContentChildren([1, 2, 3], [1, 1]),
            1,
            'Incorrect. Should be 1'
        )
        self.assertEqual(
            findContentChildren([1, 2], [1, 2, 3]),
            2,
            'Incorrect. Should be 2'
        )

    def test_containsDuplicate(self):
        self.assertEqual(
            containsDuplicate([0, 1, 2, 3, 4, 5, 0]),
            True, "Should be true"
        )
        self.assertEqual(
            containsDuplicate([11, 1, 2, 3, 4, 5, 0]),
            False,
            "Should be False"
        )

    def test_fourSum(self):
        self.assertEqual(
            four_sum([1, 0, -1, 0, -2, 2], 0),
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
            f'Incorrect Output. Expected {[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]}'
        )
        self.assertEqual(
            four_sum([2, 2, 2, 2, 2],  8),
            [[2, 2, 2, 2]],
            f'Incorrect Output. Expected {[[2,2,2,2]]}'
        )

    def test_threeSum(self):
        self.assertEqual(
            threeSum([-1, 0, 1, 2, -1, -4]),
            [[-1, -1, 2], [-1, 0, 1]],
            "Incorrect output."
        )
        self.assertEqual(threeSum([0, 1, 1]), [], "Incorrect output.")

    def test_rotatedSortedArray(self):
        array1 = [6, 7, 1, 2, 3, 4, 5]
        array2 = [6, 7, 8, 9, 1, 3, 5]
        array3 = [10, 1, 2, 3, 4, 6, 8]
        self.assertEqual(searchRotatedArray(array1, 3), 4, "Incorrect output.")
        self.assertEqual(searchRotatedArray(array2, 3), 5, "Incorrect output.")
        self.assertEqual(searchRotatedArray(array3, 3), 3, "Incorrect output.")
        self.assertEqual(searchRotatedArray(
            array3, 11), -1, "Incorrect output.")
        self.assertEqual(searchRotatedArray(
            array3, 7), -1, "Incorrect output.")

    def test_mergeSortedArray(self):
        # First sorted linked lIst
        l1_6 = ListNode(6)
        l1_4 = ListNode(4, l1_6)
        l1_2 = ListNode(2, l1_4)
        l1_0 = ListNode(0, l1_2)
        l2_5 = ListNode(5)
        l2_3 = ListNode(3, l2_5)
        l2_1 = ListNode(1, l2_3)

        ans = [0, 1, 2, 3, 4, 5, 6]
        res = mergeSortedArray(l1_0, l2_1)
        i = 0
        while res is not None:
            self.assertEqual(res.val, ans[i], "Incorrect output.")
            i += 1
            res = res.next

    def test_uniqueOccurrences(self):
        tests = [
            [1, 2, 2, 1, 1, 3],
            [1, 2],
            [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        ]
        ans = [True, False, True]
        for i in range(len(tests)):
            self.assertEqual(
                uniqueOccurrences(tests[i]),
                ans[i],
                'Incorrect output.'
            )


if __name__ == '__main__':
    unittest.main()
