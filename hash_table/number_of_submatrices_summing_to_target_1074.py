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
        pass


def main():
    tests = [
        {"nums": [[904, 1]], "target": 0, "result": 0},
        {"nums": [[0, 1, 0], [1, 1, 1], [0, 1, 0]], "target": 0, "result": 4},
        {"nums": [[1, -1], [-1, 1]], "target": 0, "result": 5},
    ]

    i = 0
    for test in tests:
        i += 1
        solver = Solution()
        print(solver.numSubmatrixSumTarget(test["nums"], test["target"]))
        assert (
            solver.numSubmatrixSumTarget(test["nums"], test["target"]) == test["result"]
        )
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
