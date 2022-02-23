code = "no"
total_cost = 0.0


def ask_number_question(question, valid_numbers, error_message):
    valid = False
    print(question)
    print(error_message)
    while not valid:
        try:
            number_entered = int(input())
            if number_entered in valid_numbers:
                return number_entered
            else:
                print(error_message)
        except ValueError:
            print(error_message)


def ask_word_question(question, valid_strings, error_message):
    valid = False
    print(question)
    while not valid:
        try:
            string_entered = str(input()).strip().lower()
            if string_entered in valid_strings:
                return string_entered
            else:
                print(error_message)
        except ValueError:
            print(error_message)


def voucher_code(question, valid_input, error_message, sorry_message):
    global total_cost
    valid = False
    print(question)
    while not valid:
        try:
            code_entered = str(input()).strip().lower()
            if code_entered in valid_input:
                total_cost -= 2
                return code_entered
            else:
                print(sorry_message)
        except ValueError:
            print(error_message)


def calculate():
    global total_cost
    if base == "thick":
        total_cost += 10
    else:
        total_cost += 8

    if base_size > 10:
        total_cost += 2

    if cheese == "no" or cheese == "n":
        total_cost -= 0.5

    if pizza_type == "vegetable" or pizza_type == "vegan":
        total_cost += 1
    elif pizza_type == "hawaiian" or pizza_type == "meat feast":
        total_cost += 2


# Main Routine
base = ask_word_question("Thin or Thick crust?", ["thin", "thick"], "Please enter Thick or Thin")
base_size = ask_number_question("What size base would you like?(sizes above 10 inches have an additional cost of $2)",
                                [8, 10, 12, 16, 18], "Please enter 8, 10, 12, 16 or 18")
cheese = ask_word_question("Would you like cheese?Y/N (No cheese will give you a $0.50 discount)", ["yes", "y", "no",
                                                                                                    "n"],
                           "Please enter Yes or No")
pizza_type = ask_word_question("What type of pizza would you like(some pizzas have additional costs)\n"
                               "Margarita = +$0.00\nVegetable = +$1.00\nVegan = +$1.00\n"
                               "Hawaiian = +$2.00\nMeat Feast = +$2.00", ["margarita", "vegetable", "vegan", "hawaiian",
                                                                          "meat feast"],
                               "Please enter Margarita, Vegetable, Vegan, Hawaiian or Meat Feast")
if base_size == 18:
    ask_user_voucher = ask_word_question("Do you have a voucher code?", ["yes", "y", "no", "n"],
                                         "Please enter Yes or No")
    if ask_user_voucher == "yes" or ask_user_voucher == "y":
        ask_voucher_code = voucher_code("Please enter the code:", ["funfriday"], "Please enter a code(no numbers)",
                                        "Sorry that is not the code")

# calculate the cost
calculate()

print("Your final cost is ${:.2f}".format(total_cost))
