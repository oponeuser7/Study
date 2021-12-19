class Solution:
    #Title: Decode String
    #Approach: String manupulation with recursion
    def decodeString(self, s: str) -> str:
        def solve(string, k):
            ans = ""
            i = 0
            while i<len(string):
                if string[i].isdigit():
                    match, count, temp = 1, "", ""
                    while(string[i].isdigit()):
                        count += string[i]
                        i += 1
                    count = int(count)
                    i += 1
                    while match:
                        if string[i]=="[": match += 1
                        if string[i]=="]": match -= 1
                        temp += string[i]
                        i += 1
                    ans += solve(temp[:len(temp)-1], count)
                    match, count, temp = 0, 0, ""
                else:
                    ans += string[i]
                    i += 1
            return k*ans
        return (solve(s, 1))
