import random as rnd

def calculate(u):
    if u==1:
        return "Legendary! You're a mind reader!"
    elif u==2:
        return "Excellent! Almost perfect!"
    elif u==3:
        return "Great job! Solid performance."
    elif u==4:
        return "Not bad! You could be faster next time."
    else:
        return "Finally! Better luck next time."



def check():
    while True:
        try:
            b=int(input("enter number between 1 and 100: "))
            if 1<=b<=100:
                return b
            else:
                print("################ warning!!, enter a number between 1 and 100 ################")
        except ValueError:
            print("################ warning!!, be sure to enter a number between 1 and 100 ################\n-------------")







def guidance(z,x):
    if -5<=z-x<=5:
        return "you are so close"
    elif -15<=z-x<=15:
        return "you are little close"
    else:
        return "you are so far"



def guess_random():
    a=rnd.randint(1,100)
    count=0
    count_check=True

    for i in range(1,6):
        print(f"-------------\nAttempt {i} of 5")
        print("enter number to guess\n-----------")
        b=check()

        if a==b:
            r=calculate(i)
            count_check=False
            return f"---- you won!    {r} ----"

        elif a>b :
            print(f"enter greater number, {guidance(a,b)}")
            count += 1
        elif a<b :
            print(f"enter less number, {guidance(a,b)}")
            count+=1

    return f"-----------------------------\nyou lose and you have used all of our chances---number was {a}"


print(guess_random())

while True:
    print("-----------------------------\ndo you want to play again?(y/n)")
    answer = str(input())
    if answer == "y" or answer == "Y":
        print(guess_random())
    elif answer=="n" or answer=="N":
        print("Goodbye!")
        break
    else:
        print("######### invalid input #########")

