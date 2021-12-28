from collections import defaultdict

class Solution:
    #Title: Group Anagrams
    #Approach: sorting
    #Explanation: Two words are anagrams if they equals when they are sorted.
    #for each word in strs, sort it and append it to a dict with key of sorted
    #word itself. By this way, you can have dict which has key of sorted word
    #and value of original words. Use collections.defaultdict to solve this. 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams["".join(sorted(word))].append(word)
        return anagrams.values()
