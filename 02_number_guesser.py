import random


def ask(question):
    number = random.randint(1, 10)
    guesses = 0
    guesses_allowed = 3
    valid = False
    while not valid:
        try:
            while guesses < 4:
                guess = int(input(question))
                guesses_allowed -= 1
                guesses += 1
                if guess == number:
                    print("Correct\nYou got it in {} guesses".format(guesses))
                    return guess
                else:
                    if guesses == 3:
                        break
                    print("Incorrect\nTry again, you have {} guesses left".format(guesses_allowed))

        except ValueError:
            print("Please enter a whole number between 1 and 10")


# Main Routine
ask("Guess a number between 1 and 10")
