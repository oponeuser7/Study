from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        day = 0
        for t in enumerate(tickets):
            q.append((t[1], t[0]))
        while q:
            day += 1
            temp = q.popleft()
            if temp[0]==1:
                if temp[1]==k:
                    return day
            else:
                q.append((temp[0]-1, temp[1]))
        return