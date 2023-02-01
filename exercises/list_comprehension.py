#TODO: use list comprehension in all of these functions
def squares():
    numbers = [1, 3, 6, 8, 12, 19, 25]
    square_numbers = []
    for num in numbers:
        square_numbers.append(num ** 2)

    print(square_numbers)


def triangle_inequality():
    values_to_test = [(2, 4, 5), (3, 4, 7), (4, 6, 8), (5, 7, 15)]
    can_be_triangle = []
    for values_set in values_to_test:
        a, b, c = values_set
        can_be_triangle.append(a + b > c and a + c > b and b + c > a)

    print(can_be_triangle)


def values_from_dicts():
    data = [{"name": "Anakin", "surname": "Skywalker", "pseudo": "Not-master", "hates": "sand"},
            {"name": "Shiv", "surname": "Palpatine", "pseudo": "Senate", "hates": "Jedi"},
            {"name": "Obi-wan", "surname": "Kenobi", "pseudo": "Highground", "hates": "lowground"},
            {"name": "Jar-jar", "surname": "Binks", "pseudo": "Darth Jar-jar", "hates": "being hated"}]
    values = []

    for entry in data:
        values.append(entry.values())

    print(values)


def long_words_from_list():
    all_words = ["Lorem", "Ipsum", "Sit", "Dolomit", "Ars", "Amas", "Apud", "Asmar",
                 "Bur", "Kek", "Loktar", "Ogar", "Zug"]
    long_words = []

    for word in all_words:
        if len(word) > 4:
            long_words.append(word)

    print(long_words)
