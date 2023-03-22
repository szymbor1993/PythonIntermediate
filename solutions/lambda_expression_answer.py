import functools


def sort_by_modulo_four_sorted(number_list):
    return sorted(number_list, key=lambda x: x % 4)


def sort_by_modulo_four_sort(number_list):
    number_list.sort(key=lambda x: x % 4)
    return number_list


def factorial(number):
    return functools.reduce(lambda prev_num, next_num: prev_num * next_num, range(1, number + 1))
