def fib(n):
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib(n - 1) + fib(n - 2)


def fib_with_case_guard(n):
    match n:
        case x if x < 2:
            return x
        case _:
            return fib(n - 1) + fib(n - 2)
