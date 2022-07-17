class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        dp = [[0] * n for _ in range(m)]
        print(dp)


def main():
    s = "12"
    print(s[1:-1])
    tests = [
        {"m": 2, "n": 2, "maxMove": 2, "startRow": 0, "startColumn": 0, "output": 6}
    ]
    i = 0
    for test in tests:
        i += 1
        solver = Solution()
        assert (
            solver.findPaths(
                test["m"],
                test["n"],
                test["maxMove"],
                test["startRow"],
                test["startColumn"],
            )
            == test["output"]
        )
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
