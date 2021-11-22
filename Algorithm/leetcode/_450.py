# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Title: Delete Node in a BST
    #There are two approaches. Iterative and Recursive.
    #Iterative: First, you have to find the node which has a value of key. After you find the key node, you need to check
    #some conditions that after deletion of a node, tree must be reorganized. If key node had no children that means the node
    #was leef node. In deletion of leef node, what you have to do is just setting the parent node of key node(I'm going to use
    #short hand "pa")'s child. But in this case, you have to compare the value between parent and key node becuase you don't know
    #if key node was a left child or a right child. This method is performed in every cases. In case which key node has a child but
    #not left and right both, you just need to set pa's left or right child to key node's left or right child. The last case is when
    #key node has both childs and this is little complex. We are going to replace key node with it's right child and atach left child
    #to the left-end of a right child. It can be guarantted that left-side tree value is always smaller than one in right-side tree by
    #definition of BST.
    #Recursive: In this approach, reorganizing of tree is much simpler. When root's val is smaller than key, recurse on left side and
    #when root's val is bigger than key, recurse on right side. The function basicly returns current node. But when you find the
    #key-matching node, returns it's left child or right child(left side tree could be attached on the bottom) or null.
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if key<root.val: root.left = self.deleteNode(root.left, key)
        elif key>root.val: root.right = self.deleteNode(root.right, key)
        else:
            if root.left and root.right:
                temp = root.right
                while temp.left: temp = temp.left
                temp.left = root.left
                return root.right
            else:
                if root.left: return root.left
                elif root.right: return root.right
                else: return None
        return root

    def deleteNode_iterative(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        pa, ans = None, root
        #find key node
        while root:
            if root.val==key: break 
            pa = root
            root = root.left if key<root.val else root.right
        #find child
        if root:
            if root.right:
                if root.left:
                    temp = root.right
                    while temp.left: temp = temp.left
                    temp.left = root.left
                if not pa: ans = root.right
                elif root.val>pa.val: pa.right = root.right
                else: pa.left = root.right
            else:
                if not pa: return root.left if root.left else None
                elif root.val>pa.val: pa.right = root.left if root.left else None
                else: pa.left = root.left if root.left else None
        return ans
