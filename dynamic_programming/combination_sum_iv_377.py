from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        dp = [1] + [0] * target
        for i in range(target + 1):
            for num in nums:
                # if num > i:
                #     break
                dp[i] += dp[i - num]
        return dp[target]


def main():
    tests = [
        {"nums": [1, 2, 3], "target": 4, "result": 7},
        {"nums": [3, 1, 2, 4], "target": 4, "result": 8},
    ]

    i = 0
    for test in tests:
        i += 1
        solver = Solution()
        print(solver.combinationSum4(test["nums"], test["target"]))
        assert solver.combinationSum4(test["nums"], test["target"]) == test["result"]
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
