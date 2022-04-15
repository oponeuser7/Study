# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Title: Trim a Binary Search Tree
    #Approach: Recursive way
    #Explanation: According to BST logic, the node with value lower than 'low'
    #makes it's whole left subtree useless(I mean to be trimed). With same
    #logic, the node with value higher than 'high' makes it's whole right
    #subtree useless. You just return the opposit side subtree. When there
    #comes a node with value in boundary, you return whole subtree.
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val>high: return self.trimBST(root.left, low, high)
        if root.val<low: return self.trimBST(root.right, low, high)
        if low<=root.val<=high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
        return None
