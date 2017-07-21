import random

roll = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
num = random.choice(roll)

print("You have three tries to guess what number the dice will roll.")

def rolldice():
    choice = input("What number do you think the dice will roll?")
    if choice == num:
        print("Correct!That is the number the dice rolled. You win!")
        exit()
    else:
        print("Incorrect! The number dice rolled is:")
        print(num)


rolldice()
print("Try again. 2 attempts remaining.")
rolldice()
print("Try again. 1 attempt remaining.")
rolldice()
print("Sorry, you lose!")
