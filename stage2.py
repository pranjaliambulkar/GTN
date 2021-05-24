#range
num1=0
num2=15
#user defined function 1
def Checkrange():
    if user in range(num1,num2):
        print("  ")
    else:
        print("YOU HAVE TO SeELECT IN RANGE OF 1-15!!!!")
#user defined function 2
def Inrange():
    if user != number:
        print("oopss!!try again!")

#program
print("welcome to stage 2")
import random
print("You have to guess the number in the range of 0 to 15")
number = random.randint(1,15)
flag=6
correct_guess=0
for i in range(0,5):
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
if correct_guess ==7:
    print("CONGRATULATIONS!!!! LEVEL COMPLETED\n stage 3:")
    import stage3