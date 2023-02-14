from typing import List

class Solution:
    
    # Complexity O(n) with convertion to string
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        return string == string[::-1]

    # Complexity O(log10 n)    
    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        n = x
        rev = 0
        while n:
            rev = rev * 10 + n % 10
            n //= 10
        return x == rev

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))

    print(solution.isPalindrome2(121))
    print(solution.isPalindrome2(-121))
    print(solution.isPalindrome2(10))