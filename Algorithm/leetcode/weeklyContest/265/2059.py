from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        visited = set()
        q = deque()
        q.append((start, 0))
        while q:
            temp = q.popleft()
            t_num = temp[0]
            count = temp[1]
            if t_num == goal:
                return count
            if not 0 <= t_num <= 1000:
                continue
            if t_num not in visited:
                visited.add(t_num)
            else:
                continue
            for num in nums:
                q.append((t_num+num, count+1))
                q.append((t_num-num, count+1))
                q.append((t_num^num, count+1))
        return -1