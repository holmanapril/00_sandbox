answer = 0
score = 0
print("Welcome to my Times Tables Quiz")
times_table = int(input("Enter a the times tables you would like to be tested on "))
maximum = int(input("Enter the maximum value of you times tables"))
print("Here is your quiz on the {} times table".format(times_table))
for x in range(1, maximum + 1):
    ask = int(input("{} times {} is ".format(x, times_table)))
    if ask == x * times_table:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

print("Your total score was {}/{}".format(score, maximum))
