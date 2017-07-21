import random

one = [1,2,3,4,5,6]
two  = [1,2,3,4,5,6]

roll = (random.choice(one) + random.choice(two))

choice = input("What number do you think the dice will roll?")
choice = int(choice)

if choice == roll:
    print("Correct!That is the number the dice rolled.")
else:
    print("Incorrect! The number dice rolled is: " + str(roll))
