# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Title: Range Sum of BST
    #Approach: DFS
    #Explanation: It is just normal dfs with condition check. You get sum
    #of tree but there is a condition when to add which is inclusive
    #range[low, high].
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node: return 0
            temp = node.val if low<=node.val<=high else 0
            return temp+dfs(node.left)+dfs(node.right)
        return dfs(root) 
