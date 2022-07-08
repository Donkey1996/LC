"""
5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.

Use a dynamic programming approach, where dp[i][j] represents whether s[i:j] is a palindrome
"""


class Solution:
    # This approach takes O(n^2) time complexity, O(n^2) space complexity, where n is the length of s
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = [[0] * len(s) for i in range(len(s))]
        ## dp[i][j] is whether s[i:j+1] is palindrome
        max_length = 1
        max_start = 0
        for i in range(length):
            dp[i][i] = 1
        for j in range(length):
            # print('i: {}'.format(i))
            for i in range(j - 1, -1, -1):
                # print('j: {}'.format(j))
                if s[i] == s[j]:
                    if dp[i + 1][j - 1] == 1 or j - i == 1:
                        dp[i][j] = 1
                        if j - i + 1 > max_length:
                            max_length = j - i + 1
                            max_start = i
        # print(max_start)
        # print(max_length)
        # print(dp)
        return s[max_start : max_start + max_length]

    def longestPalindrome2(self, s):
        ## o(n^3)
        max_length = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if self.isPalindrome(s[i : j + 1]):
                    # print(s[i:j])
                    current_length = j - i + 1
                    if current_length > max_length:
                        max_length = current_length
                        max_start = i
                        max_end = j + 1
        # print(max_length)
        return s[max_start:max_end]

    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        flag = True
        while j >= i:
            if s[i] != s[j]:
                flag = False
                break
            i += 1
            j -= 1
        return flag


def main():
    solver = Solution()
    print(solver.longestPalindrome2("abb"))
    print(solver.longestPalindrome("abbacddd"))
    print(solver.isPalindrome("aba"))


if __name__ == "__main__":
    main()
