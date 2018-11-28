"""

"""


def check_sort_increase(l):

    success = True

    for x in range(len(l)-1):
        if l[x] > l[x+1]:
            success = False
            break

    return success
