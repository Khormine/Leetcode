from typing import List

class Solution:
    
    # Complexity O(n²)
    def isValid(self, s: str) -> bool:
        dict = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for c in s:
            if c in dict.keys():
                stack.append(c)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if c != dict[a]:
                    return False
        return stack == []

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("(){}[]"))
    print(solution.isValid("(]"))