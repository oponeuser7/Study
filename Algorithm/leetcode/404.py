# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [root]
        while stack:
            temp = stack.pop()
            if not temp.left and not temp.right:
                continue
            if temp.left:
                if not temp.left.left and not temp.left.right:
                    ans += temp.left.val
                else:
                    stack.append(temp.left)
                
            if temp.right:
                stack.append(temp.right)
        return ans