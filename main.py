import random


# simple, yet effective, but doesn't make memorable passwords
def generatePassword(size=8):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ0123456789!@#$%^&*())_+-=,."
    password = ''.join(random.SystemRandom().choices(chars, k=8))
    return password


# example
password = generatePassword()
print(password)
