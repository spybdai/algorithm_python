import random
import sys

sys.path.append('..')

from utils.timer import timer
from utils.check import check_sort_increase
from sort.insertion_sort import insertion_sort, insertion_sort_less


def test_insertion_sort():

    l = [random.randint(1, 100) for _ in range(100)]
    print l

    l2 = l[:]
    print l2
    timer(insertion_sort)(l2)
    print check_sort_increase(l2)

    l3 = l[:]
    print l3
    timer(insertion_sort_less)(l3)
    print check_sort_increase(l3)


def test():
    test_insertion_sort()


if __name__ == '__main__':
    test()
