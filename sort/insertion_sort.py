"""

"""


def insertion_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j-1] > l[j]:
                l[j-1], l[j] = l[j], l[j-1]
            else:
                break


def insertion_sort_less(l):
    for i in range(1, len(l)):
        temp = l[i]
        for j in range(i, 0, -1):
            if l[j-1] > l[j]:
                l[j-1] = l[j]
            else:
                l[j] = temp
                break
