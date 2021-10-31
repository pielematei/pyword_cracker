import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890"

chars_list = list(chars)

password = input("Enter a password:")

guess = ""

while guess != password:
    guess = random.choices(chars_list, k=len(password))
    print("--- "+str(guess)+" ---")

    if guess == list(password):
        print("Cracked! Your password is: " + "".join(guess))
        break




