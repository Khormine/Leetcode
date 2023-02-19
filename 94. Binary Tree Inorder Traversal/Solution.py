from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        res, stack = [], []
        while root is not None or stack is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res

    def inorderTraversal_rec(self, root: Optional[TreeNode]) -> List[int]:
        def aux(l: List[int], node: Optional[TreeNode]):
            if  node is None:
                return
            aux(l, node.left)
            l.append(node.val)
            aux(l, node.right)        
        return aux([], root)
            


if __name__ == "__main__":
    solution = Solution()
    
    # Iterative
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(solution.inorderTraversal(root))

    root = None
    print(solution.inorderTraversal(root))
    
    root = TreeNode(1)
    print(solution.inorderTraversal(root))
    
    # Recursive
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(solution.inorderTraversal_rec(root))

    root = None
    print(solution.inorderTraversal_rec(root))
    
    root = TreeNode(1)
    print(solution.inorderTraversal_rec(root))
    
    