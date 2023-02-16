# this program demonstrates a guessing game
# random number
from random import randint

# get user input
#generate a random number 
num=randint(10,50)
# using a while loop, checkif user input = generated number 
#! get username
username=input("Enter your name: ")
print("Hello there "+ username +" ,welcome to guessing game")

# generate a random number
counter=0
while counter<5:
    usernumber=eval(input("Enter guess "))
