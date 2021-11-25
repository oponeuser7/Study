class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Title: Maximum Subarray
        #You can get sum of maximum subarray of certain index by Memoization. The sum of maximum subarray of certain index is
        #max vaule between dp[index-1] and nums[index].
        dp = [-10001]*len(nums)
        for num in enumerate(nums):
            dp[num[0]] = max(num[1], num[1]+dp[num[0]-1])
        return max(dp)
