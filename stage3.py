#range
num1=0
num2=30

#user defined function 1:
def Checkrange():
    if user in range(num1,num2):
        print("  ")
    else:
        print("You have to select in the range of 1-30")

#user defined function 2:
def Inrange():
    if user != number:
        print("OOPS!!try again!")

#user defined function 3:
def Checknum():
    if user > number:
        print("Your guess is high")
    else:
        if user < number:
            print("Your guess is lower")

#program
import random
print("You have to guess the number in the range of 0 to 30")
number = random.randint(1,30)
flag=6
correct_guess=0
for i in range(0,5):
    flag=flag-1
    print("You have",flag,"chances remaining")
    user = int(input("Guess the number"))
    Checkrange()
    Inrange()
    Checknum()
    if user == number:
        print("hurray!!!")
        print(f"You guesed the number right {number}")
        correct_guess=correct_guess+1
        break
if user!=number:
    print(f"Guess is incorrect\nCorrect number was: {number}")
if correct_guess==1:
    print("congratulations!!!!! LEVEL COMPLETED\n STAGE 4:")
    import stage4

