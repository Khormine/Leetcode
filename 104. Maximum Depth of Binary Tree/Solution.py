from typing import Optional, List
from functools import cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 1
        q = []
        q.append(root)
        height = 0
        while q != []:
            size = len(q)
            while size > 0:
                temp = q.pop()
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
                size -= 1
            height +=1
        return height
                
    @cache
    def maxDepth_rec(self, root: Optional[TreeNode]) -> int:        
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if root is None:
            return 0
        return 1 + max(self.maxDepth_rec(root.left), self.maxDepth_rec(root.right))
    
    

if __name__ == "__main__":
    solution = Solution()

    # Iterative
    root = TreeNode(3, 
                    TreeNode(9),
                    TreeNode(20, TreeNode(14), TreeNode(7)))
    print(solution.maxDepth(root))

    root = TreeNode(1, None, TreeNode(2))
    print(solution.maxDepth(root))

    # Recursive
    root = TreeNode(3, 
                    TreeNode(9),
                    TreeNode(20, TreeNode(14), TreeNode(7)))
    print(solution.maxDepth_rec(root))

    root = TreeNode(1, None, TreeNode(2))
    print(solution.maxDepth_rec(root))