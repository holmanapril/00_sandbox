
total_cost = 0.0


def base(question, choice_1, choice_2):
    error = "Please choose Thick or Thin"
    valid = False
    global total_cost
    total_cost += 2.34
    print(question)
    while not valid:
        # Check if input entered is valid
        try:
            thickness = (input())
            if thickness == choice_1 or thickness == choice_2:
                return thickness
            else:
                print(error)
        except ValueError:
            print(error)


def ask_number_question(question, valid_numbers, prompt_values):
    """Ask any question from a list of numbers\n
    Returns: integer"""
    valid = False
    print(question)
    print(prompt_values)
    while not valid:
        try:
            number_entered = int(input())
            if number_entered in valid_numbers:
                return number_entered
            else:
                print(prompt_values)
        except ValueError:
            print(prompt_values)


base("Thin or Thick crust?", "Thick", "Thin")

size_prompt = "please choose 8, 10 , 12, 14 or 18"
size = ask_number_question("What size base would you like(sizes above 10 inches have an additional cost of $2)", \
                           [8, 10, 12, 14, 18], size_prompt)

print("entered: {}".format(size))
total_cost -= 2.0
