class Solution:
    def cal_minus(self, index, prices):
        minus = 0
        for i in range(index):
            minus -= prices[i]
        return minus
        
    def maxProfit(self, prices):
        if(len(prices)<1):
            return 0
        if(len(prices)==2):
            return max(0, prices[1]-prices[0])
        if(len(prices)==3):
            return max(0, prices[1]-prices[0], prices[2]-prices[1]-prices[0])
        #시작
        max_price = 0
        max_index = 0
        for i in range(len(prices)):
            if max_price > prices[i]:
                max_price = prices[i]
                max_index = i
        for i in range(max_index+1):
            if len(prices) > 0:
                del prices[0]
        max_profit = self.cal_minus(max_index, prices)+(max_price*max_index-1)
        if len(prices) == 1:
            max_profit = max(self.cal_minus(max_index-1, prices)+(max_price*max_index-2)+prices[1]-prices[0], max_profit)
        return max_profit + self.maxProfit(prices)

solution = Solution()
print(solution.maxProfit([1,2,3,0,2]))