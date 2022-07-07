class Solution:
    def lengthOfLongestSubstring(self, s: str):
        """
        First, we initialize dictionary with every character in the string and set value to -1
        Then, we set the start position to be -1 and start count as 0
        When we loop through the string, we record the current index and compare to the start index 
        to get the length of the substring, and through a max() function we can update the max_length
        if current count is bigger than previous. 
        Before we do the compare that we need to make sure that starting point of the current count is 
        larger(behind) the last time this character appears in the string: for example, if in dict res['a'] = 10
        and start = 12, and we are currently at i = 17, we can happily include the new 'a' in the substring
        starting at 12, and do max(max_length, 17-12). However, if say the res['a'] = 15, it means the 
        count can no longer start from 12, but instead we need to ditch the last substring we are counting 
        and start with a new start index.

        Hash Table, Sliding Window

        3. Longest Substring Without Repeating Characters 
        Medium



        """
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
