class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0
        vowels = set(["a","e","i","o","u"])
        consonants = set(["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"])
        for i in range(len(word)):
            for j in range(i, len(word)+1):
                vowel_check = vowels - set(list(word[i:j]))
                consonant_check = consonants - set(list(word[i:j]))
                if len(vowel_check)==0 and len(consonant_check)==21:
                    count += 1
        return count