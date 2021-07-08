def star(t, check):
    if t==1:
        if check==True:
            return ["*"]
        else:
            return [" "]
    result = ["" for k in range(t)]

    for i in range(9):
        temp = []
        if i == 4:
            temp = star(t//3, False)
        else:
            temp = star(t//3, check)
        for j in range(len(temp)):
            if t == 3:
                result[j+i//3] += temp[j]
            else:
                result[j+int((3*(t//9))*(i//3))] += temp[j]
    return result

arr = star(int(input()), True)
for s in arr:
    print(s)