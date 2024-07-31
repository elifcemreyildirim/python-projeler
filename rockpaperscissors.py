rockpaperscissors=["rock","paper","scissors"]
import random
rock=rockpaperscissors[0]
paper=rockpaperscissors[1]
scissors=rockpaperscissors[2]
player=input("Rock? Paper? Scissors?")
x=random.choice(rockpaperscissors)

print("The computer choosed "+x)

if player==rock:
    if x==rock:
        print("scoreless")
    elif x==paper:
        print("you lost")
    else:
        print("You win")
elif player==paper:
    if x==rock:
        print("you win")
    elif x==paper:
        print("scoreless")
    else:
        print("you lost")
elif player==scissors:
    if x==rock:
        print("you lost")
    elif x==paper:
        print("you win")
    else:
        print("scoreless")
else:
    print("wrong value")
