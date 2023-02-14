from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i, d in reversed(list(enumerate(digits))):
            if d < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1,2,3]))
    print(solution.plusOne([4,3,2,1]))
    print(solution.plusOne([9]))