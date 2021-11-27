from typing import List

class Solution:
    #There are three approaches. The first one is by division. once you get the
    #total product of nums, you can get productExceptSelf by dividing. Of course
    #there lies a Divied By Zero problem. There are two cases possible. First
    #is one zero in nums. In this case, you need to calculate productExceptSelf
    #on index of zero and productExceptSelf of any other numbers would be zero.
    #The second case is two or more zero. In this case, the answer is array that
    #is just filled with bunch of zero.
    #The second approach is DP. You can do tabulation by saving products in
    #left-right order and right-left order. You can use theese two lists as
    #left and right side of productExceptSelf.
    #The third approch is by prefix. prefix is just less space version DP. You
    #pre-calculate right side of productExceptSelf and left side can be directly
    #calculated when calculating productExceptSelf.
    def productExceptSelf_space(self, nums: List[int]) -> List[int]:
        left, right, count = 1, 1, 0
        for num in nums:
            if num==0:
                count += 1
            else:
                right *= num
        product = right
        if count==0:
            for num in enumerate(nums):
                left = product//right
                right = right//num[1]
                nums[num[0]] = left*right
        elif count==1:
            for num in enumerate(nums):
                left = product//right
                right = right//(num[1] if num[1] else 1)
                nums[num[0]] = 0 if num[1] else left*right
        else:
            for i in range(len(nums)):
                nums[i] = 0
        return nums

    def productExceptSelf_time(self, nums: List[int]) -> List[int]:
        left, right = [0]*len(nums), [0]*len(nums)
        left[0], right[len(nums)-1] = 0, 0
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i]
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1]*nums[i]
        nums[0], nums[len(nums)-1] = right[1], left[len(nums)-2]
        for i in range(len(nums)):
            nums[i] = left[i-1]*right[i+1]
        return nums

    def productExceptSelf_time_space(self, nums:List[int]) -> List[int]:
        prefix = [0]*len(nums)
        prefix[len(nums)-1] = 1
        for i in range(len(nums)-1, 0, -1):
            prefix[i-1] = prefix[i]*nums[i]
        prev = 1
        for i in range(len(nums)):
            prefix[i] = prev*prefix[i]
            prev = prev*nums[i]
        return prefix
            




















