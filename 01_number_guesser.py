import random
number = random.randint(1, 10)
guesses = 0
guesses_allowed = 3
while guesses < 3:
    guess = int(input("Guess a number between 1 and 10"))
    guesses_allowed -= 1
    guesses += 1
    if guess == number:
        print("Correct\nYou got it in {} guesses".format(guesses))
        break
    else:
        if guesses == 3:
            break
        print("Incorrect\nTry again, you have {} guesses left".format(guesses_allowed))
