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


def counting_sort_stable(l):
    """
    according to specific scenario, can consider to optimize space of c
    """

    max_num, min_num = get_max_and_min(l)
    c = [0] * (max_num + 1)
    s = [0] * (len(l) + 1)

    for x in l:
        c[x] += 1

    for index in range(max_num):
        c[index+1] += c[index]

    for index in range(len(l), 0, -1):  # important, how the sort is stable
        input_val = l[index-1]
        sum_count = c[input_val]
        s[sum_count] = input_val
        c[input_val] -= 1

    return s[min_num:max_num+1]


def counting_sort_unstable(l):

    max_num, min_num = get_max_and_min(l)
    c = [0] * (max_num + 1)
    s = [0] * (len(l) + 1)

    for x in l:
        c[x] += 1

    for index in range(max_num):
        c[index+1] += c[index]

    for index in range(len(l)):  # this is not stable, pay attention to loop
        input_val = l[index]
        sum_count = c[input_val]
        s[sum_count] = input_val
        c[input_val] -= 1

    return s[min_num:max_num+1]


def counting_sort_unstable_2(l):
    """
    this function is unstable neither.
    """

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
