from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        mini = len(min(strs, key=len))
        for i in range(mini):
            c = strs[0][i]
            for word in strs:
                if word[i] != c:
                    return res
            res += c
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,2]
    print(solution.longestCommonPrefix(["flower","flow","flight"]))

    nums = [0,0,1,1,1,2,2,3,3,4]
    print(solution.longestCommonPrefix(["dog","racecar","car"]))