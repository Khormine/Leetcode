from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        return k

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeElement([3,2,2,3], 3))
    print(solution.removeElement([0,1,2,2,3,0,4,2], 2))