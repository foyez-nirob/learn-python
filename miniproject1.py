import random

number = random.randint(1,100)

count = 5
while(True):
    given = int(input("Guess the number :"))

    if (given == number):
        print("!!!!!!CONGRATULATION!!!!!, Correct number")
        break
    elif(given > number):
        print("give a smaller number(",count,"try left).")
    else :
        print("give a smaller number(",count,"try left).")
    if(count == 0):
        print("!!!Game over!!!")
        break
    count -= 1