import random
import sys

sys.path.append('..')

from utils.timer import timer
from utils.check import check_sort_increase
from sort.radix_sort import find_max, get_loop_number, radix_sort


def test_find_max():
    t = [0, 1, 15, 16, 17, 255, 256, 257, 1023, 1024, 1025]
    print find_max(t)


def test_get_max_width():
    t = [0, 1, 15, 16, 17, 255, 256, 257, 1023, 1024, 1025]
    for x in t:
        print x, get_loop_number(x)


def test_radix_sort():
    l = [random.randint(0, 999999999) for _ in range(100000)]
    timer(radix_sort)(l)
    print check_sort_increase(l)


def test():
    # test_find_max()
    # test_get_max_width()
    test_radix_sort()


if __name__ == '__main__':
    test()
