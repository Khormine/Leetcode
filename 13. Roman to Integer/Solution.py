class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
        n = len(s)
        res = map[s[n-1]]
        for i in range(n-2, -1, -1):
            if map[s[i]] >= map[s[i+1]]:
                res += map[s[i]]
            else:
                res -= map[s[i]]
        return res
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt("III"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))