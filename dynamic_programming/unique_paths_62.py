"""
62. Unique Paths
Medium

There is a robot on an m x n grid. The robot is initially located at the top-left corner 
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner 
(i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot 
can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[-1][-1]


def main():
    solver = Solution()
    assert solver.uniquePaths(3, 2) == 3
    assert solver.uniquePaths(3, 7) == 28


if __name__ == "__main__":
    main()
