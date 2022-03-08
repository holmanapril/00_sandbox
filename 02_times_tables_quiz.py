def decoration(greeting, symbol):
    # takes given greeting and symbol and puts the same amount of symbols as the amount of characters in the greeting
    greeting = "{} {} {}".format(symbol, greeting, symbol)
    top_bottom = symbol * len(greeting)

    print(top_bottom)
    print(greeting)
    print(top_bottom)


def ask_for_a_positive_int(prompt_text, error_message):
    an_int = 0
    while True:
        try:
            an_int = int(input(prompt_text))
        except ValueError:
            print(error_message)
        finally:
            if an_int > 0:
                return an_int
            else:
                print(error_message)


def questions(numbers, highest, error):
    global maximum
    global score
    # valid = False
    score = 0

    # ask for the times_table number
    times_table = ask_for_a_positive_int(numbers, error)

    # while not valid:
    #    try:
    #        maximum = int(input(highest))
    #    except ValueError:
    #        print(error)
    # ask for maximum number
    maximum = ask_for_a_positive_int(highest, error)

    print("Here is your quiz on the {} times tables".format(times_table))
    for x in range(1, maximum + 1):
        ask = ask_for_a_positive_int("{} times {} is ".format(x, times_table), "please enter a number")
        # ask for an answer
        if ask == x * times_table:
            print("Correct\n")
            score += 1
        else:
            print("Incorrect\n")


# Main Routine
global maximum
global score
decoration("Welcome to my Times Tables Quiz", "*")
questions("Enter a the times tables you would like to be tested on: ", "Enter the maximum value of you times tables:",
          "Please enter an integer(whole number)")
print("Your total score was {}/{}".format(score, maximum))
