from typing import List

from regex import F


"""
240. Search a 2D Matrix II
Medium

Write an efficient algorithm that searches for a value target in an m x n integer 
matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(mn) with some pruning, not good enough
        # m, n = len(matrix), len(matrix[0])
        # flag = False
        # for i in range(len(matrix)):
        #     print(f"i = {i}")
        #     if len(matrix[i]) > 1 and (matrix[i][0] > target or matrix[i][-1] < target):
        #         continue
        #     for j in range(len(matrix[i])):
        #         print(f'j = {j}')
        #         if matrix[i][j] == target:
        #             flag = True
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        flag = False
        while row <= m - 1 and col >= 0:
            if matrix[row][col] == target:
                flag = True
                break
            elif matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
        return flag


def main():
    tests = [
        {
            "matrix": [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            "target": 5,
            "result": True,
        },
        {
            "matrix": [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            "target": 20,
            "result": False,
        },
        {"matrix": [[1, 4], [2, 5]], "target": 5, "result": True},
    ]

    i = 0
    for test in tests:
        i += 1
        solver = Solution()
        assert solver.searchMatrix(test["matrix"], test["target"]) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
