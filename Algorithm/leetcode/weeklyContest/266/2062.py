class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set(["a","e","i","o","u"])
        ans = 0
        # for a character word[i], count of available subsets in word containing word[i] is (i+1)*(len(word)-1).
        # Explanation: When it comes to word[i]'s left side, count of subsets is (i+1). In same way, count of
        # right-side subsets is len(word)-1. By the multiplication law, the total count of subsets turns out to be
        # (i+1)*(len(word)-1). Adding this count to answer(return value) is same as adding count of vowels in some
        # amount of subsets.
        for i in range(len(word)):
            if word[i] in vowels:
                ans += (i+1)*(len(word)-i)
        return ans