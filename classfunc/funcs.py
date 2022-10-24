import random
import string


def roll_dice():
    values = []
    for num in range(6):
        values.append(random.randint(1, 6))
    return sum(values)


def password_generator(letters: int, numbers: int, puncts: int):
    chars = [random.choice(string.ascii_letters) for i in range(letters)]
    digits = [random.choice(string.digits) for i in range(numbers)]
    punct = [random.choice(string.punctuation) for i in range(puncts)]
    chars.extend(digits)
    chars.extend(punct)
    random.shuffle(chars)
    return "".join(chars)


def get_random_item(filename: str):
    with open(filename, 'r') as file:
        opened = file.readlines()
    names = [line.strip() for line in opened]
    return random.choice(names)

def generate_nickname(file1: str, file2: str):
    first_part = get_random_item(file1)
    second_part = get_random_item(file2)
    separators = ['_', '']
    result = first_part + random.choice(separators) + second_part
    return result


