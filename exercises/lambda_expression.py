import functools


def sort_by_modulo_four(number_list):
    #TODO: sort by value of modulo 4 operation, e.g. 5 mod 4 = 1.
    # Return sorted 'numbers' list.
    raise NotImplementedError()


def factorial(number):
    #TODO: return factorial of given number.
    # Use functools.reduce to accomplish this.
    # Factorial examples: 3! = 1 * 2 * 3 = 6, 5! = 1 * 2 * 3 * 4 * 5 = 120
    raise NotImplementedError()


if __name__ == "__main__":
    # exc 1
    numbers = [1, 2, 7, 8]
    sorted_numbers = [8, 1, 2, 7]
    assert sort_by_modulo_four(numbers) == sorted_numbers

    # exc 2
    assert factorial(3) == 6
    assert factorial(5) == 120
    assert factorial(12) == 479001600
