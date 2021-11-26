class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Title: Search Insert Position
        #The condition is O(logN) time complexity so you need to do binary search with index and can not use list.index like method.
        #You are going to get index(index of target - 1). Eventually, you have to do typical binary search with nums[mid] and target.
        #At last, left would be the answer.
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]<target: 
                left = mid+1
            else: 
                right = mid-1
        return left
