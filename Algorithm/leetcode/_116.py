"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from math import log2

class Solution:
    #Title: Populating Next Right Pointerrs in Each Node
    #Approach: BFS
    #Explanation: Considering input tree is perfect binary tree, there comes
    #a rule that 2^n-1th node is the rightmost node of the tree. When we use
    #bfs, we can access each nodes by level order. Save the nodes in list in
    #level order and link each nodes with next-nodes except 2^n-1th nodes. 
    #These nodes should have NULL value for next pointer.
    
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        tree = []
        queue = deque([root])
        while queue:
            temp = queue.popleft()
            if temp.left: queue.append(temp.left)
            if temp.right: queue.append(temp.right)
            tree.append(temp)
        for i, node in enumerate(tree):
            if log2(i+2)==int(log2(i+2)):
                node.next = None
            else:
                node.next = tree[i+1]
        return root
