code = "no"


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
                if string_entered == "yes" or string_entered == "y":
                    global code
                    code = "yes"
                return string_entered
            else:
                print(error_message)
        except ValueError:
            print(error_message)


def voucher_code(question, valid_input, error_message, sorry_message):
    if code == "yes":
        valid = False
        print(question)
        while not valid:
            try:
                code_entered = str(input()).strip().lower()
                if code_entered in valid_input:
                    return code_entered
                else:
                    print(sorry_message)
            except ValueError:
                print(error_message)


# Main Routine
base = ask_word_question("Thin or Thick crust?", ["thin", "thick"], "Please enter Yes or No")
base_size = ask_number_question("What size base would you like?(sizes above 10 inches have an additional cost of $2)", [8, 10, 12, 16, 18], "Please enter 8, 10, 12, 16 or 18")
cheese = ask_word_question("Would you like cheese?Y/N (No cheese will give you a $0.50 discount)", ["yes", "y", "no", "n"], "Please enter Yes or No")
pizza_type = ask_word_question("What type of pizza would you like(some pizzas have additional costs)\n"
                               "Margarita = +$0.00\nVegetable = +$1.00\nVegan = +$1.00\n"
                               "Hawaiian = +$2.00\nMeat Feast = +$2.00", ["margarita", "vegetable", "vegan", "hawaiian", "meat feast"], "Please enter Margarita, Vegetable, Vegan, Hawaiian or Meat Feast")
ask_user_voucher = ask_word_question("Do you have a voucher code?", ["yes", "y", "no", "n"], "Please enter Yes or No")
ask_voucher_code = voucher_code("Please enter the code:", ["funfriday"], "Please enter a code(only letters, no numbers)", "Sorry that is not the code")
