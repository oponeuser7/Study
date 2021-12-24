class Solution:
    #Title: Reorder Data in Log Files
    #Approach: String manipulation and sort
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []
        for log in logs:
            if log[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        letter.sort(key=lambda log:log[1:],log[0])
        digit.sort(key=lambda log:log[1:])
        return letter + digit

