# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#title: Bianry Tree Tilt
#Approach: DFS
#Explanation: To know subtree's tilt in every node, you need to make a dfs
#function which returns the sum of left, right childs and root itself.
#And at each time you get the sum of left and right subtree, calculate tilt
#between two and add it to global variable 'ans'.
class Solution:
    ans = 0
    
    def dfs(self, root):
        if not root.left and not root.right: return root.val
        left = self.dfs(root.left) if root.left else 0
        right = self.dfs(root.right) if root.right else 0
        self.ans += abs(left-right)
        return root.val+left+right
        
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.dfs(root)
        return self.ans
