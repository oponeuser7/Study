from math import log2

class Solution:
    #There is a condition that time complexity must go under O(logN). There is no other way to solve this problem
    #except binary search. Once you know approach is binary search, the point is determination logic. First, when
    #mid is odd(talking 0-index) temp num and prev num must be same and if not it means answer is in the left side.
    #When mid is even, temp num and next num must be same and if not it means answer is in the right side. You need to
    #take the corner cases when mid is left-end or right-end of nums. In these cases, it's reasonable to guese left-end
    #or right-end would be the answer. Basicly, you get anwer when temp num is diffrent with prev num and next num either.
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right,mid = 0, len(nums)-1, 0 
        while left<=right:
            mid = (left+right)//2
            if mid==0 or mid==len(nums)-1 or (nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]): break
            if (mid%2==0 and nums[mid]!=nums[mid+1]) or (mid%2==1 and nums[mid]!=nums[mid-1]):
                right = mid-1
            else:
                left = mid+1
        return nums[mid]
