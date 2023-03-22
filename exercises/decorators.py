# TODO: Write decorator(s) for the following functions, which print(s) the result to
#  the console, while keeping these functions unchanged
import functools


def squares():
    # hint: need to return value of decorated function
    numbers = [1, 3, 6, 8, 12, 19, 25]
    square_numbers = [num**2 for num in numbers]
    return square_numbers


def factorial(number):
    # hint: need to pass the argument to decorated function
    return functools.reduce((lambda prev_num, next_num: prev_num * next_num),
                            range(1, number + 1))


if __name__ == "__main__":
    print(squares())
    print(factorial(12))
