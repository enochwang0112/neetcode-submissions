# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque([root])
        sol = []

        while queue:
            q_length = len(queue)
            for i in range(q_length):
                node = queue.popleft()
                
                if i == q_length - 1:
                    sol.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return sol
            