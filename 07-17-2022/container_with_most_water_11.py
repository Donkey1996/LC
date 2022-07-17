from typing import List

"""
11. Container With Most Water
Medium
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of 
the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        i, j = 0, n - 1
        # O(n^2)
        # for i in range(n):
        #     for j in range(i, n):
        #         max_area = max(max_area, min(height[i], height[j]) * (j - i))

        ## use a while loop will be better and O(n)
        # we compare height[i] and height[j] at each iteration
        # we move the pointer only for the lower 'wall'
        
        while i <= j:
            max_area = max(max_area, min(height[i], height[j])*(j-i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_area


def main():
    solver = Solution()
    tests = [
        {"height": [1,1], "result": 1},
        {"height": [1,8,6,2,5,4,8,3,7], "result": 49},
    ]
    i = 0
    for test in tests:
        i += 1
        assert solver.maxArea(test["height"]) == test["result"]
        print("Passed solver test {}".format(i))


if __name__ == "__main__":
    main()
