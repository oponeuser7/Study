class Solution:
    #Title: Single Number
    #Approach: Bit Manipulation
    #Explanation: You can figure out which is the appeared-once number by
    #keep "XOR"ing numbers in array. By the logic of XOR, there eventually
    #lefts appeared-once number only.
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans = ans^num
        return ans
            
