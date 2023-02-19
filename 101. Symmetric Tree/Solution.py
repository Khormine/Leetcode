from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric_rec(self, root: Optional[TreeNode]) -> bool:        
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        def aux(right: Optional[TreeNode], left: Optional[TreeNode]) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return aux(left.left, right.right) and aux(left.right, right.left)          
        
        if root is None:
            return True
        return aux(root.left, root.right)

if __name__ == "__main__":
    solution = Solution()

    root = TreeNode(1, 
                    TreeNode(2, TreeNode(3), TreeNode(4)),
                    TreeNode(2, TreeNode(4), TreeNode(3)))
    print(solution.isSymmetric_rec(root))

    root = TreeNode(1, 
                    TreeNode(2, None, TreeNode(3)),
                    TreeNode(2, None, TreeNode(3)))
    print(solution.isSymmetric_rec(root))