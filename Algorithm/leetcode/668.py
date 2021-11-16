class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        #By the fact that rows can be expressed like [1*i, 2*i, 3*i, ..., n*i], you can figure out the order
        #of random number X. It's same as the count of numbers which are smaller than X. In ith row, the count
        #of numbers which are smaller than X is X//i. But it could overwhelm the row length n so tactically it
        #should be min(X//i, n). So, the sum of min(X//i, n) in every rows would be the numer X's place. We are
        #going to name this solution count(X).
        #But using this method for every single possible number would cost O(n^2) time so we supposed to use
        #binary search. By binary search you would be able to find count(X) which is greater than K. You should
        #keep binary search to find the X which has minimum count(X) which is greater than K and it would be the
        #answer.
        left, right = 0, m*n
        ans = 0
        while left<=right:
            mid = (left+right)//2
            temp = sum([min(num//i, n) for i in range(1,m+1)])
            if temp<k:
                left = mid+1
            else:
                right = mid-1
                ans = mid
        return ans