from collections import deque, defaultdict
from typing import List

"""
746. Min Cost Climbing Stairs
Easy

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

2 <= cost.length <= 1000
0 <= cost[i] <= 999

"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        at step i, you can either take two steps from i-2 or one step from i-1. 
        we have the dp relationship dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        dp[0] = 0, dp[1] = dp[0] + cost[0]
        
        """
        n = len(cost) # steps
        dp = [0 for i in range(n + 1)]
        # dp[1] = cost[0]

        for i in range(2, n+1):
            dp[i] = min(
                dp[i-1] + cost[i-1],
                dp[i-2] + cost[i-2]
            )
            
        return dp[-1]
    
    def solve(self, input):
        results = self.minCostClimbingStairs(cost=input)
        return results



def main():
    tests = [
        {'cost': [1,100,1,1,1,100,1,1,100,1], 'result': 6},
        {'cost': [10, 15, 20], 'result': 15}
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
