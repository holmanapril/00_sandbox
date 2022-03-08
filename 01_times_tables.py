answer = 0

times_table = int(input("Enter a the times tables you would like to see"))
print("Here is the {} times table".format(times_table))
for x in range(1, 13):
    answer = x * times_table
    print("{} times {} is {}".format(x, times_table, answer))
