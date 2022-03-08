import random


def decoration(greeting, symbol):
    # takes given greeting and symbol and puts the same amount of symbols as the amount of characters in the greeting
    sides = symbol
    greeting = "{} {} {}".format(sides, greeting, sides)
    top_bottom = symbol * len(greeting)

    print(top_bottom)
    print(greeting)
    print(top_bottom)


def ask(question):
    global number
    global guesses_allowed
    number = random.randint(1, 10)
    guesses = 0
    guesses_allowed = 3
    print(question)
    valid = False
    while not valid:
        try:
            while guesses < 3:
                guess = int(input())
                print()
                guesses += 1
                guesses_allowed -= 1
                if guess == number:
                    decoration("Correct", "*")
                    print("You got it in {} guesses".format(guesses))
                    print()
                    return guess
                else:
                    decoration("Incorrect", "-")
                    if guess < number:
                        print("Hint: The number is higher than {}".format(guess))
                    else:
                        print("Hint: The number is lower than {}".format(guess))

                    if guesses_allowed == 0:
                        return guess
                    print("Try again, you have {} guesses left".format(guesses_allowed))
                    print()

        except ValueError:
            print("Please enter a whole number between 1 and 10")


# def hint():
    # global guess
    # if guess < number:
        # print("Hint: The number is higher than {}".format(guess))


# Main Routine
decoration("Welcome to this number guesser", "!")
global guesses_allowed
global number
ask("Guess a number between 1 and 10")
if guesses_allowed == 0:
    print()
    print("The correct number was {}".format(number))
decoration("Thank you for playing", "!")
