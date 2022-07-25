from collections import deque, defaultdict
from typing import List

"""
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def searchRange(self, nums, target):
        l = self.search_left(nums, target)
        r = self.search_right(nums, target)
        return [l, r]

    def search_left(self, nums, target):
        left_index = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                left_index = m
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return left_index

    def search_right(self, nums, target):
        left_index = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                left_index = m
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return left_index


def main():
    tests = [
        {"nums": [5, 7, 7, 8, 8, 10], "target": 8, "result": [3, 4],},
        {"nums": [5, 7, 7, 8, 8, 10], "target": 6, "result": [-1, -1],},
        {"nums": [0, 0, 1, 1, 2, 3], "target": 0, "result": [0, 1],},
        {"nums": [1], "target": 0, "result": [-1, -1]},
        {"nums": [2, 2], "target": 3, "result": [-1, -1]},
    ]

    i = 0
    for test in tests:
        i += 1
        solver = Solution()
        print(solver.search_left(test["nums"], test["target"]))
        print(solver.search_right(test["nums"], test["target"]))
        assert solver.searchRange(test["nums"], test["target"]) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
