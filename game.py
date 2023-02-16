# this program demonstrates a guessing game
# random number
from random import randint

# get user input
#generate a random number 

# using a while loop, checkif user input = generated number 
#! get username
username=input("Enter your name: ")
print("Hello there "+ username +" ,welcome to guessing game")
num=randint(10,50)
# generate a random number
counter=0
while counter <5:
    usernumber=eval(input("Enter guess "))
    counter += 1
    if usernumber < num:
        print("too low")
    elif usernumber>num:
        print("too high")
    elif usernumber==num:
        print(" you win!")
        break        