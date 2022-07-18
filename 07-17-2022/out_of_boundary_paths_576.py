"""
576. Out of Boundary Paths
Medium

There is an m x n grid with a ball. The ball is initially at the position 
[startRow, startColumn]. 
You are allowed to move the ball to one of the four adjacent cells in the grid 
(possibly out of the grid crossing the grid boundary). 
You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, 
return the number of paths to move the ball out of the grid boundary. 
Since the answer can be very large, return it modulo 109 + 7.
"""


class Solution:
    """
    Three-dimensional DP

    recursive with base conditions right out of the boundary
    we return 1 if the goal state is reached
    0 if max move is reached

    """

    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        dp = [[[-1] * n for _ in range(m)] for _ in range(maxMove)]
        mod = 10 ** 9 + 7
        return self._find_paths(dp, m, n, 0, maxMove, startRow, startColumn) % mod

    def _find_paths(self, dp, m, n, curMove, maxMove, i, j):
        if i < 0 or j < 0 or i >= m or j >= n:
            return 1
        if curMove >= maxMove:
            return 0
        if dp[curMove][i][j] != -1:
            return dp[curMove][i][j]
        dp[curMove][i][j] = (
            self._find_paths(dp, m, n, curMove + 1, maxMove, i - 1, j)
            + self._find_paths(dp, m, n, curMove + 1, maxMove, i + 1, j)
            + self._find_paths(dp, m, n, curMove + 1, maxMove, i, j - 1)
            + self._find_paths(dp, m, n, curMove + 1, maxMove, i, j + 1)
        )
        return dp[curMove][i][j]


def main():
    tests = [
        {"m": 2, "n": 2, "maxMove": 2, "startRow": 0, "startColumn": 0, "output": 6},
        {"m": 5, "n": 5, "maxMove": 5, "startRow": 0, "startColumn": 0, "output": 64},
    ]
    i = 0
    for test in tests:
        i += 1
        solver = Solution()
        print(
            solver.findPaths(
                test["m"],
                test["n"],
                test["maxMove"],
                test["startRow"],
                test["startColumn"],
            )
        )
        assert (
            solver.findPaths(
                test["m"],
                test["n"],
                test["maxMove"],
                test["startRow"],
                test["startColumn"],
            )
            == test["output"]
        )
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
