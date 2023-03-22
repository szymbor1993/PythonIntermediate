def squares(numbers):
    return [num ** 2 for num in numbers]


def triangle_inequality(values_to_test):
    return [a + b > c and a + c > b and b + c > a for a, b, c in values_to_test]


def values_from_dicts(list_of_dicts):
    return [entry.values() for entry in list_of_dicts]


def long_words_from_list(words_list):
    return [word for word in words_list if len(word) > 4]
