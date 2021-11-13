from collections import deque

class Solution:
    #Used stack to slove problem. You traverse through list inverse. If
    #current temperature is lower than temperature of stack top, that means
    #the day of stack top is the day temperature rises. And you push current
    #temperature and it would be the highest temperature of the future from
    #the view of day i-1. if current temperature is higher than temperature of
    #stack top, you pop until the stack is empty or the temperature of stack top
    #is higher than current one. After this process, stack top would be the anwer
    #of that time.
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = deque()
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            ans[i] = 0 if not stack else stack[-1] - i
            stack.append(i)
        return ans