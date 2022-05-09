from collections import Counter
from collections import deque

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        q = deque()
        for num in nums:
            q.append(num)
        c = Counter(q)
        
