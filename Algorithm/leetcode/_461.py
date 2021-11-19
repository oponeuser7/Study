from math import log2

#Basicly this is a bit operation problem. First, what you need to know is the positions where the bit differs
#between two numbers and XOR operation will do. The outcome of XOR supposed to be have exactly n bits of value 1
#which is the count of diffrent bits between two numbers. Then how do we count 1? Prepare a number 1 and do AND
#operation between temp and 1. If result is true that means the bit on that position is 1. Then left shift number 1 and
#go on. You need to iterate log2(temp)+1 times that it is number of bits in temp.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        temp = x^y
        if temp==0: return temp
        for i in range(int(log2(temp))+1):
            if temp & 1 << i: ans += 1
        return ans
