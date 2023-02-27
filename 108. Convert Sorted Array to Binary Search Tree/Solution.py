from typing import Optional, List
from functools import cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums is None:
            return None
        
        def aux(nums, start, end):
            if start > end:
                return None
            mid = (start + end + 1) // 2
            root = TreeNode(nums[mid])
            root.left = aux(nums, start, mid - 1)
            root.right = aux(nums, mid + 1, end)
            return root
        
        return aux(nums, 0, len(nums) - 1)