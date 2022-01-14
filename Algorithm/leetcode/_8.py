class Solution:
    #Title: String to Integer(atoi)
    #Approach: string manipulation
    def myAtoi(self, s: str) -> int:
        sign = 1
        num = 0
        num_flag = False
        for c in s:
            if c.isdigit():
                num_flag = True
                num = num*10+int(c)
            else:
                if not num_flag:
                    if c==" ": continue
                    elif c=="+":
                        num_flag = True
                        continue
                    elif c=="-":
                        num_flag = True
                        sign = -1
                        continue
                    break
                break
        num *= sign
        if num>=0:
            if num>2**31-1: num = 2**31-1
        else:
            if num<-(2**31): num = -(2**31)
        return num

