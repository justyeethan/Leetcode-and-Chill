"""
Write an efficient algorithm that searches for a value in an m x n
matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of
the previous row.

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

"""

def matrix_search(matrix, target):
    """
    l1/r1 = pointers to find the column BSearch
    l2/r2 = pointers to find the row BSearch
    """
    res = False
    COL, ROW = len(matrix), len(matrix[0])

    l1, r1 = 0, COL
    selected_column = []

    while l1 < r1:
        mid = l1 + ((r1 - l1) // 2)
        if matrix[mid][0] < target < matrix[mid][-1]:
            selected_column = matrix[mid]
            break
        elif target < matrix[mid][0]:
            r1 = mid
        elif target > matrix[mid][-1]:
            l1 = mid + 1

    l2, r2 = 0, len(selected_column)
    while l2 < r2:
        mid = l2 + ((r2-l2) // 2)
        if selected_column[mid] > target:
            r2 = mid
        if selected_column[mid] < target:
            l2 = mid
        else:
            res = True
            break
    return res

if __name__ == "__main__":
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    test1 = matrix_search(matrix, 22)
    assert test1 == False, "Wrong input."
