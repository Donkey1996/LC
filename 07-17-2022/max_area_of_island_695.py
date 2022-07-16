from typing import List

"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid 
are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        This is a DFS problem
        We start with traversing the grid one by one.
        when we see a 1 cell, we 'sink' the cell and keep searching the neighbors until 
        all 1 cells in the current island are visited.

        search(i,j) will return the area of the area of the island with current cell index
        as part of the island. 
    

        """
        m, n = len(grid), len(grid[0])

        def search(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return (
                1
                + search(i - 1, j)
                + search(i, j - 1)
                + search(i, j + 1)
                + search(i + 1, j)
            )

        max_area = 0
        for i in range(m + 1):
            for j in range(n + 1):
                try:
                    if grid[i][j] == 1:
                        max_area = max(max_area, search(i, j))
                except:
                    pass
        print(max_area)
        return max_area


def main():
    solver = Solution()
    tests = [
        {
            "grid": [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ],
            "result": 6,
        },
        {"grid": [[1]], "result": 1,},
        {"grid": [[0, 0, 1, 1, 0, 1, 1, 1, 0, 0]], "result": 3,},
    ]
    i = 0
    for test in tests:
        i += 1
        assert solver.maxAreaOfIsland(test["grid"]) == test["result"]
        print("Passed solver test {}".format(i))


if __name__ == "__main__":
    main()
