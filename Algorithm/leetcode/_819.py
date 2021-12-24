from collections import Counter
import re

class Solution:
    #Title: Most Common Word
    #Approach: String manipulation with regular expression and Counter,
    #list comprehension.
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        paragraph = re.sub("\W"," ",paragraph).lower().split()
        p = [word for word in paragraph if word not in banned]
        return Counter(p).most_common(1)[0][0]
