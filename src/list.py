import random


def generate_random_list(n, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(n)]
