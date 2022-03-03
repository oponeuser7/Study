from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = set()
        queue = deque()
        ans = Node(node.val, node.neighbors)
        queue.append(ans)
        while queue:
            cur = queue.popleft()
            visited.add(cur.val)
            for neighbor in cur.neighbors:
                if neighbor.val not in visited:
                    queue.append(Node(neighbor.val, neighbor.neighbors))
        return ans
