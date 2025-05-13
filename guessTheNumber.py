import random
print("~~~~~~~~~~~~GUESS THE NUMBER GAME~~~~~~~~~~~~~~~~~~")

print("let me think of a number btwn 1 to 100.\n")
no=random.randint(1,100)
level=input("Choose the level of difficulty.....Type 'easy' or 'hard':\n")
if(level=='easy'):
    attempts=10
elif(level=='hard'):
    attempts=5
won=False
while(attempts!=0 and won==False):
    print(f"You have {attempts} attempts remaining to guess the number\n\n")
    guess=int(input("MAKE A GUESS:"))
    if(guess<no):
        print("Your guess is lower than the number I have generated")
        print("Guess again\n\n")
        attempts-=1
    elif(guess>no):
        print("Your guess is greater than the number I have generated")
        print("Guess again\n\n")
        attempts-=1
    elif(guess==no):
        print("You guessed the number correctly\n----CONGRAGULATIONS YOU WON----\n")
        won=True
    else:
        print(f"Sorry...THE ANS WAS {no}")

