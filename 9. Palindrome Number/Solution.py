from typing import List

class Solution:
    
    # Complexity O(n) with convertion to string
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        return string == string[::-1]
    

solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))