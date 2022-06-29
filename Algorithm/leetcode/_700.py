# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            temp = stack.pop()
            if temp.val==val: return temp
            if temp.left: stack.append(temp.left)
            if temp.right: stack.append(temp.right)
        return None
    def searchBST_recursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val==val: return root
        return self.searchBST_recursive(root.reft if root.val>val else root.right, val)
