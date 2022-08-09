from collections import defaultdict
from typing import List

"""
1074. Number of Submatrices That Sum to Target
Hard

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and 
y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have 
some coordinate that is different: for example, if x1 != x1'.
"""


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/303750/JavaC%2B%2BPython-Find-the-Subarray-with-Target-Sum
        
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
        res = 0
        for i in range(n):
            for j in range(i, n):
                current_sum = 0
                dictionary = {0: 1}
                for k in range(m):
                    current_sum += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    if current_sum - target in dictionary:
                        res += dictionary[current_sum - target]
                    if current_sum in dictionary:
                        dictionary[current_sum] += 1
                    else:
                        dictionary[current_sum] = 1
        return res


def main():
    tests = [
        {"nums": [[0, 1, 0], [1, 1, 1], [0, 1, 0]], "target": 0, "result": 4},
        {"nums": [[904, 1]], "target": 0, "result": 0},
        {"nums": [[1, -1], [-1, 1]], "target": 0, "result": 5},
    ]

    i = 0
    for test in tests:
        i += 1
        solver = Solution()

        assert (
            solver.numSubmatrixSumTarget(test["nums"], test["target"]) == test["result"]
        )
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
