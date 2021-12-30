class Solution:
    #Title: Smallest Integer Divisible by K
    #Approach: math
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0: return -1
        n = 1
        for i in range(1, 500000):
            if n%k==0: return i
            n = n*10+1
        return -1
