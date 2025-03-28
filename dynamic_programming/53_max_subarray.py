from collections import deque, defaultdict
from typing import List
from math import inf

"""

53. Maximum Subarray
Medium

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        The key to recognize here is that you want to keep a copy of current iteration of the subarray.
        While keeping a global max of the sum.
        
        """
        current_max = 0
        max_until_now = -inf

        for c in nums:
            # if the new element is bigger than the abs value of the current (negative) sum, just start over. otherwise just keep adding 
            current_max = max(current_max + c, c)
            # keep the global copy of max sum
            max_until_now = max(current_max, max_until_now)

        return max_until_now
        

    
    def solve(self, input):
        results = self.maxSubArray(nums=input)
        return results



def main():
    tests = [
        {'cost': [-2,1,-3,4,-1,2,1,-5,4], 'result': 6},
        {'cost': [5,4,-1,7,8], 'result': 23}
    ]

    i = 0
    for test in tests:
        i += 1
        solver = Solution()
        try: 
            result = solver.solve(test['cost'])
            assert(result == test['result'])
            print(f"Passed test case {i}")
        except:
            print(f"Wrong answer: {result}. Correct Answer: {test['result']}")
        # assert solver.solve(test["cost"]) == test["result"]


if __name__ == "__main__":
    main()
