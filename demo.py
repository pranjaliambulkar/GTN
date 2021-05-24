#range
num1=0
num2=10
#user defined function 1
def Checkrange():
    if user in range(num1,num2):
        print("  ")
    else:
        print("YOU HAVE TO SELECT IN THE RANGE OF  1-10!!!")
#user defined function 2
def Inrange():
    if user != number:
        print("oopss!!try again!")

#program
from random import *
number = randint(1,10)
flag=7
correct_guess=0
for i in range(0,6):
    flag=flag-1
    print("You have",flag,"chances remaining")
    user = int(input("Guess the number"))
    Inrange()
    Checkrange()
    if user == number:
        print("HURRAY!!!")
        print(f"You guesed the number right {number}")
        correct_guess=correct_guess+1
        break
if user!=number:
    print(f"Guess is incorrect\nCorrect number was: {number}")
if correct_guess==1:
    print("CONGRATULATIONS!!! LEVEL COMPLETEd")
    import stage2
