# 97. Interleaving String; medium
"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

"""


class Solution:
    def __init__(self) -> None:
        pass

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # DP
        """
        dp[i][j] is whether s3[:i+j] interleaves at s1[:i] and s2[:j]
        """
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len1 + len2 != len3:
            return False

        dp = [[False for j in range(len2 + 1)] for i in range(len1 + 1)]
        for i in range(len1 + 1):
            # notice the index here is important so that list dont go out of range
            for j in range(len2 + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    # on the first row, we look left for true, then also need current last word in s2 and s3 matches each other
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    # first column, same deal
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    # in field, just do or from both directions
                    dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (
                        dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                    )
        return dp[len1][len2]


def main():
    solver = Solution()
    tests = [
        {"s1": "aabcc", "s2": "dbbca", "s3": "aadbbcbcac", "result": True},
        {"s1": "aabcc", "s2": "dbbca", "s3": "aadbbbaccc", "result": False},
        {"s1": "", "s2": "", "s3": "", "result": True},
    ]
    i = 0
    for test in tests:
        i += 1
        output = solver.isInterleave(test["s1"], test["s2"], test["s3"])
        assert test["result"] == output
        print("Passed Test #{}!".format(i))


if __name__ == "__main__":
    main()
