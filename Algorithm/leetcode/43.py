class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # don't know why but in case of len() like functions which have O(1) time complexity was much faster
        # when it's called multiple times rather than using it's result stored in a variable. It seems insane
        # becuase this means that fetching value of a variable which is memory(or could be register) access 
        # is slower than a function. 
        ans = 0
        op1 = 0
        for i in range(len(num1)):
            op1 += int(num1[len(num1)-1-i]) * (10**i)
        for i in range(len(num2)):
            ans += op1 * int(num2[len(num2)-1-i]) * (10**i)
        return str(ans)