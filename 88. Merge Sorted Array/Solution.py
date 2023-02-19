from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Time complexity: O(n+m)
        Space complexity: O(1)
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
            


if __name__ == "__main__":
    solution = Solution()
    nums1, nums2, = [1,2,3,0,0,0], [2,5,6]
    m, n = 3, 3 
    solution.merge(nums1, m, nums2, n)
    print(nums1)
    
    nums1, nums2, = [1], []
    m, n = 1, 0 
    solution.merge(nums1, m, nums2, n)
    print(nums1)
    
    nums1, nums2, = [0], [1]
    m, n = 0, 1 
    solution.merge(nums1, m, nums2, n)
    print(nums1)