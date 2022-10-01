from os.path import abspath


def count_lines(name):
    with open(name, "r") as file:
        value = len(file.readlines())
    return value


def count_chars(name):
    with open(name, "r") as file:
        values = len(file.read().replace("\n", ""))
    return values


def test(name):
    path = abspath(name)
    chars = count_chars(path)
    lines = count_lines(path)
    return chars, lines
