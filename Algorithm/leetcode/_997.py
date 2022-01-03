class Solution:
    #Title: Find the Town Judge
    #Approach: Array, Hash Table
    #Explanation: The town judge is basicly most trusted person in town which
    #means town judge is the person who appeared most in trust[i][1]. And the
    #amount of trust must be exactly n-1. And mostly, town judge must trust
    #nobody. According to this fact, we need to have boolean table to record
    #that someone trusts the other. In summary, the town judge is the person
    #who is trusted n-1 times and is not in trusts-table.
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        votes = [0]*(n+1)
        voted = [False]*(n+1)
        for t in trust:
            votes[t[1]] += 1
            voted[t[0]] = True
        ans, _max = 1, 0
        for i, vote in enumerate(votes):
            if _max<vote: 
                ans = i
                _max = vote
        return ans if _max==n-1 and not voted[ans] else -1
