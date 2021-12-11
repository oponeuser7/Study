from math import lcm

class Solution:
    #Title: Nth Magical Number
    #Approach: Binary Search
    #Why?: If you try brute-force approach you will know that maximum time
    #comlexity would be O(N*max(a,b)) and it is linear time already while
    #having time limit problem at the same time. Which means we should achieve
    #either O(logN) or O(1) time complexity and the later one would be kinda
    #impossible so we can make a reasonable guess that this is a binary search
    #problem. Now the point is how to know the order of random number i. We
    #can know that there are i//a numbers before i and i//b also but this is
    #not the answer. a and b can have common multiples. So you need to subtract
    #(i//(lcm(a,b)) from i//a+i//b.
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def check(mid, a, b, n):
            temp = mid//a + mid//b + mid//(lcm(a,b))
            return n<=temp

        ans, left, right = 0, 2, max(a,b)*1000000000
        while(left<=right):
            mid = (left+right)//2
            if check(mid, a, b, n):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans
