import re

def fname_sort(fname_list):
    p = re.compile("(\D+)(\d+)")
    return sorted(fname_list, key=lambda x:(p.match(x).group(1).lower(), int(p.match(x).group(2))))
fname_list = list(x.strip() for x in input().strip().split(','))
print(*fname_sort(fname_list))