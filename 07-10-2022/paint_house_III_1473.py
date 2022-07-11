'''
There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
Given an array houses, an m x n matrix cost and an integer target where:

houses[i]: is the color of the house i, and 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j + 1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.

'''


from typing import List
import pytest


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        return 0
    
    def test1(self):
        res = self.minCost(houses=[], cost=[[]], m=1, n=1, target=1)
        print(res)
        assert 1 == 1


def main():
    solver = Solution()
    solver.test1()
    pytest.main(["-q", "paint_house_III_1473.py"])


if __name__ == "__main__":
    main()
