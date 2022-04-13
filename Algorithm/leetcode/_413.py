class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        prev, diff, counter, ans = 0, 3000, 0, 0
        for num in nums:
            if diff==abs(num-prev) or diff==3000:
                counter += 1
                if counter >= 3: ans += counter-2
                diff = abs(num-prev)
            else: 
                counter = 1
                diff = 3000
            prev = num
        return ans
