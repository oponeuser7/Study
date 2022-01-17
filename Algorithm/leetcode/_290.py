class Solution:
    #Title: Word Pattern
    #Approach: string manipulation, Hash table
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = {}
        seen = set()
        words = s.split()
        index = 0
        for p in pattern:
            if index>len(words)-1: return False
            if p not in table:
                if words[index] in seen: return False
                table[p] = words[index]
                seen.add(words[index])
                index += 1
            else:
                if table[p]!=words[index]: return False
                index += 1
        if index==len(words): return True
        return False
