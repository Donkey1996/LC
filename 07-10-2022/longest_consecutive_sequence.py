from typing import List

"""128. Longest Consecutive Sequence; Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


class Solution:
    """
    StefanPochmann:
    if n-1 not in nums makes sure that you prune some of the repetitive calcs. 
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        for n in nums:
            if n - 1 not in nums:
                m = n + 1
                while m in nums:
                    m += 1
                max_length = max(max_length, m - n)
        return max_length


def main():
    solver = Solution()
    tests = [
        {"nums": [1, 2, 3, 4, 5, 7, 8, 9], "result": 5},
        {"nums": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], "result": 9},
    ]
    i = 0
    for test in tests:
        i += 1
        output = solver.longestConsecutive(test["nums"])
        assert test["result"] == output
        print("Passed Test #{}!".format(i))


if __name__ == "__main__":
    main()
