class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        rows = [""]*numRows
        adder = -1
        i = 0
        for c in s:
            rows[i] += c
            if i%(numRows-1)==0:
                adder *= -1
            i += adder
        return "".join(rows)