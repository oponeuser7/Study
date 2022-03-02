class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        limit = len(s)
        cur = 0
        for c in t:
            if cur==limit: return True
            if c==s[cur]: cur += 1
        return cur==limit
