import random
import sys

sys.path.append('..')

from utils.timer import timer
from sort.counting_sort import get_max_and_min, counting_sort, counting_sort_2


def test_get_max_and_min():
    l = [random.randint(1, 10) for _ in range(10)]
    max_num, min_num = get_max_and_min(l)
    print max_num, min_num


def test_counting_sort():
    l = [random.randint(1, 10) for _ in range(10)]
    l2 = l[:]

    timer(counting_sort)(l)
    for x in range(len(l)-1):
        if l[x] > l[x+1]:
            print 'FAIL!'
            break
    print 'SUCCESS!'

    timer(counting_sort_2)(l2)
    for x in range(len(l2)-1):
        if l2[x] > l2[x+1]:
            print 'FAIL!'
            break
    print 'SUCCESS!'


def test():
    # test_get_max_and_min()
    test_counting_sort()


if __name__ == '__main__':
    test()
