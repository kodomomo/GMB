import random

english = ['A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']

nums = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


def generate_random_secret():
    secret = ''
    _kr_key = random.choice(english)
    for _ in range(2): secret += random.choice(nums)
    secret += _kr_key
    for _ in range(3): secret += random.choice(nums)

    return secret
