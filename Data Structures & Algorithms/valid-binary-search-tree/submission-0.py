# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, high, low) -> bool:
            if node is None:
                return True
            elif low < node.val < high:
                return isValid(node.left, node.val, low) and isValid(node.right, high, node.val)
            else:
                return False
        
        return isValid(root, 1001, -1001)