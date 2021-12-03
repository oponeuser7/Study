from typing import List

class Solution:
    #Title: Maximam Product Subarray
    #Solution: DP
    #Why?: You might think of DP when you first saw the problem. When solving
    #DP problems it's important to define the subproblem. In this problem, sub
    #problem is the max product subarray of subarray. There is no way merging
    #two subproblems I see, so it would be O(N) time straight-iterative problem
    #. In this kind of DP problems, some technic with sparkling idea like 'If
    # it is A, it would never be B'. In this problem, regarding current index
    # as i, if max product till i-1 is smaller than sole number at i, max pro
    #duct till i-1 can never be the answer. And other key point is that you
    #need to keep the minimum value of max product since it could turn into
    #maximum number by multiplying two negative numbers. By this method, you
    #would always be able to keep track of maximum product subarray at index i.
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        _min, _max = 1, 1
        for num in nums:
            way = (num, num*_max, num*_min)
            _max, _min = max(way), min(way)
            ans = max(ans, _max)
        return ans
