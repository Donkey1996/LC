from typing import List

"""
560. Subarray Sum Equals K
Medium

Given an array of integers nums and an integer k, return the total number of 
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        prefix sum with hashmap

        dictionary stores all the calculated paths to sum to k.
        with 0 set to initial one, everytime cumsum - k is in dictionary,
        dictionary[cumsum-k] variations were already calculated.

        https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example
        """
        dictionary = {0: 1}
        cumsum = 0
        res = 0
        for num in nums:
            cumsum += num
            if cumsum - k in dictionary:
                res += dictionary[cumsum - k]
            if cumsum in dictionary:
                dictionary[cumsum] += 1
            else:
                dictionary[cumsum] = 1
        return res


def main():
    tests = [
        {"nums": [1, 1, 1], "target": 2, "result": 2},
        {"nums": [1, 2, 3], "target": 3, "result": 2},
    ]

    i = 0
    for test in tests:
        i += 1
        solver = Solution()
        print(solver.subarraySum(test["nums"], test["target"]))
        assert solver.subarraySum(test["nums"], test["target"]) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
