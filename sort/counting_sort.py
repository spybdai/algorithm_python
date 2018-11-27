"""
counting sort
"""


def get_max_and_min(l):
    max_num = min_num = l[0]
    for x in l:
        if max_num < x:
            max_num = x
        elif min_num > x:
            min_num = x
    return max_num, min_num


def counting_sort(l):

    max_num, min_num = get_max_and_min(l)
    k = max_num - min_num + 1
    c = [0] * k

    for x in l:
        c[x - min_num] += 1

    pointer = 0
    for index in range(len(c)):
        for _ in range(c[index]):
            value = index + min_num
            l[pointer] = value
            pointer += 1


def counting_sort_2(l):

    print l
    max_num, _ = get_max_and_min(l)
    c = [0] * (max_num + 1)
    s = c[:]

    for x in l:
        c[x] += 1

    for index in range(max_num):
        c[index+1] += c[index]

    for index in range(len(l), 0, -1):
        origin_val = l[index-1]
        count_val = c[origin_val]
        s[count_val-1] = origin_val

    l[:] = s
    print l
