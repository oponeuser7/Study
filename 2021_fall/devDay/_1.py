def solution(s):
    s = s.split()
    pages, back, front = [0]*100, [], []
    for c in s:
        if c=='B':
            if len(back)>1:
                temp = back.pop()
                pages[back[-1]] += 1
                front.append(temp)
        elif c=='F':
            if front:
                temp = front.pop()
                pages[temp] += 1
                back.append(temp)
        else:
            front = []
            pages[int(c)] += 1
            back.append(int(c))
    return max(pages)
