from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''
        s = strs[0]
        for c in s:
            flag = True
            for si in strs:
                flag = flag and self.start_with(si, common_prefix+c)
                if flag == False:
                    break
            if flag == True:
                common_prefix += c
        return common_prefix
            
    def start_with(self, s, pre):
        if s[:len(pre)] == pre:
            return True
        else:
            return False


def main():
    tests = [
        {'strs': ['flower', 'floor', 'flight'], 'prefix': 'fl'},
        {'strs':['dogs', 'cat'], 'prefix': ''},
        {'strs':['dog', 'dogshit'], 'prefix': 'dog'},

    ]
    i = 0
    solver = Solution()
    for test in tests:
        i += 1
        assert solver.longestCommonPrefix(test['strs']) == test['prefix']
        print(f'passed test {i}')

if __name__ == '__main__':
    main()