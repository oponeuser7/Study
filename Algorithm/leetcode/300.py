class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # It's a DP problem. Here is the adea. At index j, LIS is Max value of LISs' from the
        # left side of index j + 1. All index's LIS are initially 1. Once you find a LIS which is greater
        # than or equal to LIS index j - 1, you change LIS index j. By this way(memoization), all index's 
        # LIS would be calculated and Max value of this LIS list would be the answer.
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j]<nums[i] and dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
        return max(dp)