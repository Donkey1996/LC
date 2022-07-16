"""
7. Reverse Integer
not interesting
"""

from re import M
from sympy import solve


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1, -1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2 ** 31) - 1 < rst < 2 ** 31 else 0


def main():
    solver = Solution()

    print(solver.reverse(8848))


if __name__ == "__main__":
    main()
