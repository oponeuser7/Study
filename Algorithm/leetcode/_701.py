# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Title: Insert into a Binary Search Tree
    #Approach: Recursive
    #Explanation: This function returns a left or right subtree by the rule of
    #Binary Search Tree. If val is bigger than root.val return right subtree
    #and left subtree for the opposit way. Then when the root becomes null,
    #create new node with value of val and return it.
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        if val<root.val: root.left = self.insertIntoBST(root.left, val)
        else: root.right = self.insertIntoBST(root.right, val)
        return root
