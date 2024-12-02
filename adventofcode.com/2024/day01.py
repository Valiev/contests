# from math import abs
from helpers import input_filepath


def list_distance(list1, list2):
    distance = 0
    for l1, l2 in zip(sorted(list1), sorted(list2)):
        distance += abs(l1 - l2)
    return distance

def list_distance_with_counter(list1, counter):
    distance = 0
    for elem in list1:
        if elem not in counter:
            continue
        distance += elem * counter[elem]
    return distance


def calc_distance_01(input_file):
    list1, list2 = [], []
    for line in open(input_file):
        if not line.strip():
            continue
        l1, l2 = line.strip().split()
        list1.append(int(l1))
        list2.append(int(l2))
    return list_distance(list1, list2)


def calc_distance_02(input_file):
    list1 = []
    l2_counter = dict()
    for line in open(input_file):
        if not line.strip():
            continue
        l1, l2 = line.strip().split()
        l1, l2 = int(l1), int(l2)
        list1.append(l1)
        l2_counter[l2] = 1 + l2_counter.get(l2, 0)

    return list_distance_with_counter(list1, l2_counter)


if __name__ == "__main__":
    input_file = input_filepath("day01.txt")
    print(calc_distance_01(input_file))
    print(calc_distance_02(input_file))
