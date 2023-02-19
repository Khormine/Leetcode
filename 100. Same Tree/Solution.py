from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(min(|p|,|q|))
        Space complexity: O(1)
        """
        if p is None and q is None:
            return True
        if p is None or q is  None:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)            


if __name__ == "__main__":
    solution = Solution()

    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = p
    print(solution.isSameTree(p, q))

    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    print(solution.isSameTree(p, q))
    
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    print(solution.isSameTree(p, q))
    
    