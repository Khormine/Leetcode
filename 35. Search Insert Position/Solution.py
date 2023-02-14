from typing import List

class Solution:
    # dichotomie => O(log n)
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while(start <= end):
            mid = (start + end)//2
            # found target
            if nums[mid] == target:
                return mid
            elif target >= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        # insertion position
        return end + 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert([1,3,5,6], 5))
    print(solution.searchInsert([1,3,5,6], 2))
    print(solution.searchInsert([1,3,5,6], 7))