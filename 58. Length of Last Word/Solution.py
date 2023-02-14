class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.split(" ")
        final = [w for w in temp if w != '']
        return len(final[-1])

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord("Hello World"))
    print(solution.lengthOfLastWord("   fly me   to   the moon  "))
    print(solution.lengthOfLastWord("luffy is still joyboy"))