def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

word1 = input().strip().lower().replace(" ","")
word2 = input().strip().lower().replace(" ","")
print(word1, word2)
if(is_anagram(word1, word2)):
    print(1)
else:
    print(0)