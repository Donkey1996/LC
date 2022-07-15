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
        pass

def main():
    solver = Solution()
    tests = [
        {'s': 'III', 'result': 3},
        {'s': 'LVIII', 'result': 58},
        {'s': 'MCMXCIV', 'result': 1994}
    ]
    i = 0
    for test in tests:
        i+=1
        assert solver.romanToInt(test['s']) == test['result']
        print('Passed solver test {}'.format(i))


if __name__ == '__main__':
    main()