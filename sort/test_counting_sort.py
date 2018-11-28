import random
import sys

sys.path.append('..')

from utils.timer import timer
from utils.check import check_sort_increase
from sort.counting_sort import get_max_and_min, counting_sort_stable_strict, counting_sort_stable, \
    counting_sort_unstable, counting_sort_unstable_2


def test_get_max_and_min():
    l = [random.randint(1, 10) for _ in range(10)]
    max_num, min_num = get_max_and_min(l)
    print max_num, min_num


def test_counting_sort():
    l = [random.randint(1, 100000) for _ in range(1000000)]

    l_sorted = timer(counting_sort_stable_strict)(l)
    print check_sort_increase(l_sorted)

    l_sorted = timer(counting_sort_stable)(l)
    print check_sort_increase(l_sorted)

    l_sorted = timer(counting_sort_unstable)(l)
    print check_sort_increase(l_sorted)

    timer(counting_sort_unstable_2)(l)
    print check_sort_increase(l)


def test():
    # test_get_max_and_min()
    test_counting_sort()


if __name__ == '__main__':
    test()
