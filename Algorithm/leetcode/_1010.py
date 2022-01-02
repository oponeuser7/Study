class Solution:
    #Title: Pair of Songs With Total Durations Divisible by 60
    #Approach: Hash table, Combinations 
    #Explanation: First you might think of brute force approach but it ends up
    #with time out. Then here is a fact that if sum of two numbers are
    #divisible by 60, sum of remainders of each numbers are also divisible by
    #60. You need to calculate remainders of numbers in list which is O(N) time
    #complexity and save it as a counter. I used array to do this. Then
    #in range 1~60 count of divisibles would be counter[i]*counter[60-i]/2.
    #There are corner cases where i is 0 and 30. in these cases undistinctable
    #two numbers are paired so that you need to use combination to count.
    #It is actually count[i] Combinations 2. To fit these cases with normal 
    #cases, you need to multiply 2 to these cases and divide 2 from final
    #answer.
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        def combination(m):
            return math.factorial(m)//(2*math.factorial(m-2))
        ans = 0
        counter = [0]*61
        for i in time:
            counter[i%60] += 1
        for i in range(60):
            if (i==30 or i==0) and counter[i]>1:
                ans += combination(counter[i])*2
            else:
                ans += counter[i]*counter[60-i]
        return ans//2
