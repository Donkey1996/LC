from typing import List

"""

4. Median of Two Sorted Arrays; Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""


class Solution:
    """
    break it down by making a recursive findKthSmallest() function that finds the kth smallest element in the two sorted arrays
    The indexing is very important
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            # if odd number in total, then we return the (n+1)/2 th element, which is indexed at (n-1)/2
            return self.findKthSmallest(nums1, nums2, (l - 1) // 2)
        else:
            # if even number, return 1/2 of n/2, n/2 + 1 elements
            return (
                (
                    self.findKthSmallest(nums1, nums2, l // 2)
                    + self.findKthSmallest(nums1, nums2, l // 2 - 1)
                )/2
            )

    def findKthSmallest(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k]
        if len(nums2) == 0:
            return nums1[k]
        index1, index2 = len(nums1) // 2, len(nums2) // 2
        median1, median2 = nums1[index1], nums2[index2]

        if index1 + index2 < k:
            if median1 > median2:
                # first half of nums2 is eliminated
                # notice the index in the recursion call is k-index1/2-1, as we eliminated index1/2+1 smaller components
                return self.findKthSmallest(nums1, nums2[index2 + 1 :], k - index2 - 1)
            else:
                # first half of nums1 is eliminated
                return self.findKthSmallest(nums1[index1 + 1 :], nums2, k - index1 - 1)
        else:
            if median1 > median2:
                # second half of the nums1 is eliminated
                # notice here we use k, as we only eliminated the bigger components
                return self.findKthSmallest(nums1[:index1], nums2, k)
            else:
                # second half of nums2 eliminated
                return self.findKthSmallest(nums1, nums2[:index2], k)


def main():
    solver = Solution()
    tests = [
        {"nums1": [1, 3], "nums2": [2], "result": 2},
        {
            "nums1": [
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                11,
                12,
                13,
                14,
                155,
                1556,
                22222,
                44534,
                53345,
            ],
            "nums2": [1, 2, 3, 4, 5, 6, 7, 111, 2222, 3333, 4444, 5555, 7777],
            "result": 10,
        },
    ]
    i = 0
    for test in tests:
        i += 1
        output = solver.findMedianSortedArrays(test["nums1"], test["nums2"])
        assert test["result"] == output
        print("Passed Test #{}!".format(i))


if __name__ == "__main__":
    main()
