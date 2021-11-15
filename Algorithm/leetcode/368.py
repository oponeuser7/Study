class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # It's a DP problem. First, you need to sort the nums list since we are going to see if a number
        # in certain index is divisible by index -  1 number. If prev number is larger than next one there
        # would be no point cause it will always be divisible. Here is the idea. nums[i]'s well nevermind
        # It's too hard to explain in english.
        nums.sort()
        dp = [[num] for num in nums]
        _max = 0
        ans = [nums[0]]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(dp[j])+1>len(dp[i]):
                    dp[i] = dp[j]+[nums[i]]
                    if len(dp[i])>_max:
                        _max = len(dp[i])
                        ans = dp[i]
        return ans