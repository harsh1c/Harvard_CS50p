import random
import sys

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
            else:
                continue
        except (ValueError, TypeError):
            continue

    random_number = random.randint(1, int(n))
    check_guess(random_number)

def check_guess(random_number):

    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                break
            else:
                continue

        except (ValueError, TypeError):
           continue

    while True:
        try:
            if guess < random_number:
                print("Too small!")
                guess = int(input("Guess: "))

            elif guess > random_number:
                print("Too large!")
                guess = int(input("Guess: "))

            else:
                print("Just right!")
                sys.exit()
        except (ValueError, TypeError):
            check_guess(random_number)

main()