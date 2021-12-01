from typing import List

class Solution:
    #Title: House Rober
    #Approach: DP
    #Why?: When you think simple, the possibilies are combination of choosing
    #between next number or next next number. But when nums.length could be
    #100 at max, the time complexity could be 2^100 at max and it is insane.
    #But if you look closely, you would know that there are redundant 
    #operation. When you have calculated max value of random index i, it is
    #same as you calculated answer which has a argument of list nums[i:].
    #And this is the subproblem of this DP problem.
    
    def rob(self, nums: List[int]) -> int:
        pprev, prev = 0, 0
        for num in nums:
            cur = max(num+pprev, prev)
            pprev = prev
            prev = cur
        return cur
