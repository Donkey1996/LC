class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return self.is_palindrome_stirng(str(x))

    def is_palindrome_string(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        return self.is_palindrome_string(s[1:-1]) and s[0] == s[-1]
