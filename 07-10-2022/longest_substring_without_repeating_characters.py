class Solution:
    def lengthOfLongestSubstring(self, s: str):
        res = {c: -1 for c in s}
        start = -1
        max_length = 0
        for i in range(len(s)):
            if res[s[i]] > start:
                start = res[s[i]]
            res[s[i]] = i
            max_length = max(max_length, i - start)
        return max_length


def main():
    solver = Solution()
    tests = [{"s": "abcabcbb", "result": 3}, {"s": "pwwkew", "result": 3}]
    i = 0
    for test in tests:
        i += 1
        output = solver.lengthOfLongestSubstring(test["s"])
        assert test["result"] == output
        print("Passed Test #{}!".format(i))


if __name__ == "__main__":
    main()
