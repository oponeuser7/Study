class Solution:
    #Title: Car Pooling
    #Approach: Array
    #Explanation: Consider a 2d graph which has a length of 1000. And for each
    #trips do increament and decreament for from and to indexes with amount of 
    #numPassengers. Then itrerate through graph and keep adding graph[i] to
    #temp. temp is the temporal amount of passangers and if it is larger than
    #capacity then the answer might be False.
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans = [0]*1001
        for num, frm, to in trips:
            ans[frm] += num
            ans[to] -= num
        temp = 0
        for i in ans:
            temp += ans
            if temp>capacity: return False
        return True
