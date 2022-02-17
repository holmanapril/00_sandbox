def base(question, choice_1, choice_2):
    error = "Please choose Thick or Thin"
    valid = False
    while not valid:
        # Check if input entered is valid
        try:
            thickness = (input(question))
            if thickness == choice_1 or thickness == choice_2:
                return thickness
            else:
                print(error)
        except ValueError:
            print(error)


def size(question, choice_1, choice_2, choice_3, choice_4, choice_5):
    error_2 = "please choose 8, 10 , 12, 14 or 18"
    valid = False
    while not valid:
        try:
            pizza_size = int(input(question))
            if pizza_size == choice_1 or pizza_size == choice_2 or pizza_size == choice_3 or pizza_size == choice_4 or pizza_size == choice_5
                return pizza_size
        except ValueError:
            print(error_2)


int(input("What size base would you like(sizes above 10 inches have an additional cost of $2)\n"
          "Sizes: 8, 10, 12, 14, 18").lower())
cheese = input("Would you like cheese?Y/N (No cheese will give you a $0.50 discount)").lower()
pizza_type = input("What type of pizza would you like(some pizzas have additional costs)\n"
                   "Margarita = +$0.00\nVegetable = +$1.00\nVegan = +$1.00\n"
                   "Hawaiian = +$2.00\nMeat Feast = +$2.00").lower()
if base == "thick":
    total_cost = 10
else:
    total_cost = 8

if size > 10:
    total_cost += 2

if cheese == "y":
    total_cost -= -0.5

if pizza_type == "vegetable" or pizza_type == "vegan":
    total_cost += 1
elif pizza_type == "hawaiian" or pizza_type == "meat feast":
    total_cost += 2

if size == 18:
    voucher = input("Do you have a voucher code?").lower()
    if voucher == "yes" or voucher == "y":
        code = input("What is the code?(Make sure to use correct capitals)")
        if code == "FunFriday":
            total_cost -= 2
print(total_cost)
base("Thin or Thick crust?", "Thick", "Thin")
size("What size base would you like(sizes above 10 inches have an additional cost of $2)\n"
     "Sizes: 8, 10, 12, 14, 18", 8, 10, 12, 14, 18)
