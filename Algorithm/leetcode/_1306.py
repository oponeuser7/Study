from typing import List
from collections import deque

class Solution:
    #title: Jump Game III
    #Approach: BFS
    #Why?: When it is given that you need to find vaild route from certain
    #start point to end point, you might think of graph search. This is just
    #two-demensional version of graph search. You can jump from node to node
    #using current node vaule and you can't go outside the graph. Just keep
    #doing visit check and if you found zero which is the answer, return True.
    #And if while loof has just ended, return False.
    def canReach(self, arr: List[int], start: int) -> bool:
        l = len(arr)
        queue = deque([start])
        visited = [False]*l
        while queue:
            i = queue.popleft()
            val = arr[i]
            if val==0: return True
            if 0<=i-val<l and not visited[i-val]:
                queue.append(i-val)
                visited[i-val] = True
            if 0<=i+val<l and not visited[i+val]:
                queue.append(i+val)
                visited[i+val] = True
        return False
