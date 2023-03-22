import functools


def print_to_console(func):
    def wrapper(*args):
        ret_val = func(*args)
        print(f"Decorator returns: {ret_val}")
        return ret_val
    return wrapper


@print_to_console
def squares():
    numbers = [1, 3, 6, 8, 12, 19, 25]
    square_numbers = [num**2 for num in numbers]
    return square_numbers


@print_to_console
def factorial(number):
    return functools.reduce((lambda prev_num, next_num: prev_num * next_num), range(1, number + 1))
