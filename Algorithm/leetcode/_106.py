# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Title: Construct Binary Tree from Inorder and Postorder Traversal
    #The information you can get from post-order is that the last element of post-order is the root node. And the information that
    #you can get from in-order is that from position of root node in in-order result, it's left side happens to be left-side tree and
    #right side turns out to be right-side tree. So there could be a recursive approach. First you get the root node from post-order
    #search results and divide tree by left and right using in-order search results. And for left and right each, do a recurive function
    #call. 
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder return None
        root = inorder.index(postorder[-1])
        left = buildTree(inorder[:root], postorder[:root])
        right = buildTree(inorder[root+1:], postorder[root:len(postorder)-1])
        return TreeNode(inorder[root], left, right)

