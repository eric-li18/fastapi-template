import random, string


def random_string():
    return "".join(random.choices(string.ascii_letters, k=32))


def random_float(upper: float = 100.0):
    return random.uniform(0.0, upper)