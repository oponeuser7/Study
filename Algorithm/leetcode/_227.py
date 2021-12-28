class Solution:
    def calculate(self, s: str) -> int:
        def cal(a, b, op):
            if op=="+": return a+b
            elif op=="-": return a-b
            elif op=="*": return a*b
            elif op=="/": return a/b
            else: return None

        order = {"*":1,"/":1,"+":2,"-":2}
        digit = []
        op = []
        flag = False
        for c in s:
            if c.isdigit():
                if flag:
                    digit[-1] = digit[-1]*10+int(c)
                else:
                    digit.append(int(c))
            else:
                if not op or order[op[-1]]>order[c]:
                    op.append(c)
                else:
                    while order[op[-1]]<=order[c]:
                        a = digit.pop()
                        b = digit.pop()
                        digit.append(cal(a,b,op.pop()))
        while op:
            a = digit.pop()
            b = digit.pop()
            digit.append(cal(a,b,c))
        return digit[0]

