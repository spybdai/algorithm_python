"""
Radix sort, with 16 as radix

show the workflow of algorithm, so, try not to use python libs or built-in functions
"""


def find_max(l):
    mx = 0
    for x in l:
        if mx < x:
            mx = x
    return mx


def get_loop_number(num):
    """
    how many loops need.
    """
    c = 0
    while num:
        c += 1
        num >>= 4
    if not c:
        return 1
    return c


def radix_sort(l):
    max_number = find_max(l)
    loop_number = get_loop_number(max_number)

    for x in range(loop_number):
        buckets = [[] for _ in range(16)]  # need 16 buckets.
        for num in l:
            buckets[(num >> 4 * x) & 15].append(num)
        del l[:]  # reuse original list
        for bucket in buckets:
            l.extend(bucket)
