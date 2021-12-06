from collections import Counter

class Solution:
    #Title: Minimum Cost to Move Chips to The Same Position
    #Approach: math I guess
    #Explanation: I have two approaches, brute-force and math. Let's talk
    #about brute-force first. In brute-force approach, you need to find every
    #cost to move from every nodes except node 'x' to node 'x' which takes
    #O(N^2) time complexity. The formula of cost is simple. If distance is odd
    #the cost is 1 and if even the cost is 0. But we can make it in O(N) time
    #by optimization. Let's think of it. If you choose not to move certain node
    #and if it's index is odd, all even index nodes will cost and same goes for
    #the opposit. Which means, there is actually only two choices you have.
    #Odd nodes or even nodes. You need to count number of odd and even coins
    #and return smaller value and it would be the answer.
    def minCostToMoveChips_brute_force(self, position: List[int]) -> int:
        ans = float("inf")
        counter = Counter(position)
        print(counter)
        for i in counter:
            temp = 0
            for j in counter:
                if i==j: continue
                temp += (abs(i-j)%2)*counter[j]
            ans = min(temp, ans)
        return ans

    def minCostToMoveChips(self, position: List[int]) -> int:
            odd, even = 0, 0
            for i in position:
                if i%2==0: even += 1
                else: odd += 1
            return min(odd, even)
