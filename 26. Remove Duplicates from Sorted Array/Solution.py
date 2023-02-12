from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        res = []
        for n in nums:
            if n not in nums[:k:]:
                nums[k] = n
                k+=1
        return k

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,2]
    print(solution.removeDuplicates(nums), nums)

    nums = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(nums), nums)