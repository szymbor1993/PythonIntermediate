#TODO: rewrite functions to use list comprehension
def squares(numbers):
    square_numbers = []
    for num in numbers:
        square_numbers.append(num ** 2)

    return square_numbers


def triangle_inequality(values_to_test):
    can_be_triangle = []
    for values_set in values_to_test:
        a, b, c = values_set
        can_be_triangle.append(a + b > c and a + c > b and b + c > a)

    return can_be_triangle


def values_from_dicts(list_of_dicts):
    values = []
    for entry in list_of_dicts:
        values.append(entry.values())

    return values


def long_words_from_list(words_list):
    long_words = []
    for word in words_list:
        if len(word) > 4:
            long_words.append(word)

    return long_words


if __name__ == "__main__":
    # exercise 1
    number_list = [1, 3, 6, 8, 12, 19, 25]
    print(squares(number_list))

    # exercise 2
    triangle_sides = [(2, 4, 5), (3, 4, 7), (4, 6, 8), (5, 7, 15)]
    print(triangle_inequality(triangle_sides))

    # exercise 3
    data = [{"name": "Anakin", "surname": "Skywalker", "pseudo": "Not-master",
             "hates": "sand"},
            {"name": "Shiv", "surname": "Palpatine", "pseudo": "Senate",
             "hates": "Jedi"},
            {"name": "Obi-wan", "surname": "Kenobi", "pseudo": "Highground",
             "hates": "lowground"},
            {"name": "Jar-jar", "surname": "Binks", "pseudo": "Darth Jar-jar",
             "hates": "being hated"}]
    print(values_from_dicts(data))

    # exercise 4
    all_words = ["Lorem", "Ipsum", "Sit", "Dolomit", "Foo", "Bar", "Baz", "Asmar",
                 "Bur", "Kek", "Loktar", "Ogar", "Zug"]
    print(long_words_from_list(all_words))
