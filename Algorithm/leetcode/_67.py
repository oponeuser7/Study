class Solution:
    #Title: Add Binary
    #Approach: Bit manipulation
    #Explanation: When you want to add two binary numbers and get result with
    #decimal value, you just need to add each bit with same position as decimal
    #value. There is no explicit zero in string-formed input so you consider
    #string out-of-range index as a zero bit.
    def addBinary(self, a: str, b: str) -> str:
        ans = 0
        for i in range(max(len(a), len(b))):
            op1 = int(a[len(a)-1-i]) if len(a)-i>0 else 0
            op2 = int(b[len(b)-1-i]) if len(b)-i>0 else 0
            ans += (op1<<i) + (op2<<i)
        return bin(ans)[2:]

