# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [(root, root.val)]
        while stack:
            temp = stack.pop()
            node = temp[0]
            number = temp[1]
            if not node.left and not node.right:
                ans += number
                continue
            if node.left:
                stack.append((node.left, number*10+node.left.val))
            if node.right:
                stack.append((node.right, number*10+node.right.val))
        return ans