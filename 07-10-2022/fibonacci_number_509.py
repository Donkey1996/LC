from re import L
import pytest
import sys


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        fib = [0] * (n + 1)
        fib[1] = 1
        for i in range(n - 1):
            fib[i + 2] = fib[i] + fib[i + 1]
        return fib[-1]


def test1():
    solver = Solution()
    tests = [
        {"n": 1, "result": 1},
        {"n": 2, "result": 1},
        {"n": 5, "result": 5},
        {"n": 8, "result": 21},
        {"n": 25, "result": 75025},
    ]
    for i in range(len(tests)):
        assert solver.fib(tests[i]["n"]) == tests[i]["result"]
        # print('Passed test #{}'.format(i))


def test2():
    assert 1 == 1


def main():
    pytest.main(["-q", "fibonacci_number_509.py"])


if __name__ == "__main__":
    main()
