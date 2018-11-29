import random
import sys

sys.path.append('..')

from utils.timer import timer
from utils.check import check_sort_increase
from sort.insertion_sort import insertion_sort


def test_insertion_sort():

    l = [random.randint(1, 1000) for _ in range(1000)]
    timer(insertion_sort)(l)
    print check_sort_increase(l)


def test():
    test_insertion_sort()


if __name__ == '__main__':
    test()
