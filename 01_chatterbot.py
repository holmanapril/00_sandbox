name = input("What is your name?").lower()
if name == "anakin":
    print("How do you do Anakin!")
elif name == "leia":
    print("The force is with you")
else:
    print("Nice name, {}.".format(name))

weather = input("So {}, is it hot or cold where you are today?".format(name)).upper()
if weather == "COLD":
    print("You must be freezing!")
elif weather == "HOT":
    print("Drink plenty of water")
else:
    print("I can't advise you on that type of weather.")

likes_blue = input("Do you like the colour blue?").upper()
if likes_blue == "YES":
    print("I like blue too")
else:
    print("That's a shame, I really like blue")

print("Have a good day! Bye!")
