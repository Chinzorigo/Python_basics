# 16 characters password generator

import random


def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ""
    for i in range(16):
        password += random.choice(characters)
    return password


print(generate_password())
