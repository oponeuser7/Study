class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(s: str) -> bool:
            for i in range(len(s)//2):
                if s[i]!=s[len(s)-i-1]: return False
            return True
        def find(s: str) -> 
