from math import log2

class Solution:
    #Title: Power of Two
    #Approach: math
    #Explanation: An integer n is power of two if there exists an integer x
    #such that n==2^x. This means that an integer n is power of two if log2 n
    #is natural number. n could be negative or zero and in these cases answer
    #must be false.
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: return False
        return log2(n)==int(log2(n))
