class Solution:
    #The problem is simple but there is a trick to solve in O(1) space complexity.
    #Length of the input list is N and it's elements must fit the scope (1,N). Which means the index could
    #represent the single numbers of scope(1,N). By negating list[list[index]+1], you can save the fact that
    #number of index has appeared. Sole thing left to do is appending positive numbers from input list to ans list.
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num)-1]>0: nums[abs(num)-1] *= -1 
        for num in enumerate(nums):
            if num[1]>0: ans.append(num[0]+1)
        return ans