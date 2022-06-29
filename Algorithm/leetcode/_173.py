# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
        
    def __init__(self, root: Optional[TreeNode]):
        this.rooot = TreeNode()
        rooot.right = root

    def next(self) -> int:
        rooot = rooot.right
        return rooot.val

    def hasNext(self) -> bool:
        return rooot.right
