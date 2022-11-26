import random
import time

user = 0
computer = 0
tied = 0
name = input("Give me your name : ")
print("Hi",name,"Welcome to Rock Paper Scissors game with Computer")
print("In this game you'll get 10 chances against computer")
lst = ["rock","paper","scissor"]

i = 10
while i > 0:
    comp = random.choice(lst)
    i -= 1
    choice = input("Select R for Rock, S for Scissor, P for Paper : ")
    if choice.lower() == "r":
        if comp == "rock":
            tied += 1
            print("both have rock, No Point")
        elif comp == "paper":
            computer += 1
            print("Computer gets a point")
        else:
            user +=1
            print("You get a point")
    elif choice.lower() == "p":
        if comp == "paper":
            tied += 1
            print("both have paper, No Point")
        elif comp == "scisscor":
            computer += 1
            print("Computer gets a point")
        else:
            user +=1
            print("You get a point")
    elif choice.lower() == "s":
        if comp == "scissor":
            tied += 1
            print("both have scissor, No Point")
        elif comp == "rock":
            computer += 1
            print("Computer gets a point")
        else:
            user +=1
            print("You get a point")
time.sleep(3)
if user > computer:
    print("You won the game")
elif computer > user:
    print("Computer won the game, Better Luck next time!")
else:
    print("Its a Draw")
print("Your Points :",user)
print("Computer Points :",computer)
print("Tied games :",tied)
time.sleep(10)