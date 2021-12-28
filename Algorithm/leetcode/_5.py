class Solution:
    #Title: Longest Palindromic Substring
    #Approach: Two pointers
    #Explanation: Use two sliding windows. One has length of 2 and 3 for the
    #other one. At each points, sliding windows check if first character and
    #last character are equal and if it is, window expands itself and repeat
    #this untill the condition is false. Using this strategy we can get the
    #longest palindromic substring in point x. Answer is the max value of len
    #gth of these substrings.
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2 or s==s[::-1]: return s
        def expand(left: int, right: int) -> str:
            while left>=0 and right<len(s) and s[left]==s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        ans = ""
        for i in range(len(s)-1):
            ans = max(ans, expand(i,i+1), expand(i,i+2), key=len)
        return ans

