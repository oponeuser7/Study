import re

def dart(s):
    p = re.compile("(\d+)([a-zA-Z])(\*|\#)?")
    p = p.findall(s)
    result = []
    for i in range(3):
        temp = int(p[i][0])
        if p[i][1] == 'D':
            temp *= temp
        elif p[i][1] == 'T':
            temp *= temp * temp
        if p[i][2] == '*':
            temp *= 2
            if i > 0:
                result[i-1] *= 2
        elif p[i][2] == '#':
            temp *= -1
        result.append(temp)
    return result[0] + result[1] + result[2]
s = input()
print(dart(s))