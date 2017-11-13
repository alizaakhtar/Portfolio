import random
import time

layer1 = ["red","black"]
layer2 = ["odd","even"]

output1 = random.choice(layer1)
output2 = random.choice(layer2)
output3 = random.randint(1,36)
money = 500
print("Welcome to online Roulette. You have $500 to bet and can play 3 times.")

def game():
    global money
    bet = input("What kind of bet would you like to make? a) red or black, b) odd or even, c) specific number?")
    if bet == "a":
        layer1bet = input("Would you like to guess red or black?")
        money1 = input("How much money would you like to bet?")
        money1 = int(money1)
        print("Standby while the ball is rolling.")
        time.sleep(2)
        if layer1bet == output1:
            money = money + money1
            print("Congratulations! You were correct! You win " + str(money1))
            print("Now you have $" + str(money))
        else:
            money = money - money1
            print("Sorry, you were incorrect. The correct color was " + output1)
            print("You lost $" + str(money1))
            print("Now you have $" + str(money))

    if bet == "b":
        layer2bet = input("Would you like to guess odd or even?")
        money2 = input("How much money would you like to bet?")
        money2 = int(money2)
        print("Standby while the ball is rolling.")
        time.sleep(2)
        if layer2bet == output2:
            money = money + money2
            print("Congratulations! You were correct! You win " + str(money2))
            print("Now you have $" + str(money))
        else:
            money = money - money2
            print("Sorry, you were incorrect. The correct answer was " + output2)
            print("You lost $" + str(money2))
            print("Now you have $" + str(money))

    if bet == "c":
        layer3bet1 = input("What number, between 1 and 36, would you like to guess?")
        money3 = input("How much money would you like to bet?")
        money3 = int(money3)
        print("Standby while the ball is rolling.")
        time.sleep(2)
        if layer3bet1 == output3:
            money = money + money3
            print("Congratulations! You were correct! You win " + str(money3))
            print("Now you have $" + str(money))
        else:
            money = money - money3
            print("Sorry, you were incorrect. The correct number was " +str(output3))
            print("You lost $" + str(money3))
            print("Now you have $" + str(money))

game()
time.sleep(2)

game()
time.sleep(2)

game()
time.sleep(2)

if money > 0:
    print("Congrats, you still have this much money remaining: $" + str(money))
elif money == 0:
    print("Sorry, you lost all of your money.")
else:
    print("Oh no! You are in debt. This is how much money you owe: $" + str(money))

exit()
