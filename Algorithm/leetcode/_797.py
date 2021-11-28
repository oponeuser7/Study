from typing import List
from collections import deque

class Solution:
    #Title:All Paths From Source to Target
    #This is a graph search problem and there is no cycle and direction in graph
    #. This means that you don't need to do visit check. BFS or DFS will be the
    #solution. You push a path to stack and every time you visit child, copy
    # the path list child appended and push it to stack. When crrurent path's
    # last index is target, you can add this path to answer.
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)
        stack = deque([[0]])
        while stack:
            temp = stack.pop()
            node, path = temp[-1], temp
            if node==n-1:
                ans.append(path)
                continue
            for child in graph[node]:
                new_path = path[:]
                new_path.append(child)
                stack.append(new_path) 
        return ans
