total_cost = 0
base = input("Thin or Thick crust?").lower()
size = int(input("What size base would you like(sizes above 10 inches have an additional cost of $2)\n"
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
