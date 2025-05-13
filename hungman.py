import random

print("WELCOME TO HUNGMAN GAME!!!!")

list=["suryaprasad",'priyadarshini','lokesh','Ningamani','chandrakala']
word=random.choice(list)

print("The choosen word has length of ",len(word))
blank=[]
for i in range(len(word)):
    blank.append('_')
print(blank)

life=5
newWord=''
while(life!=0 and newWord!=word):
    a=input("Guess the letter:\n")
    if(a not in word):
        life-=1
        print(f"Sorry,{a} is not in the word you have {life} life now!!!")
    else:
         for index, letter in enumerate(word):#look at enumerate file
            if letter == a:
                blank[index] = a
        
    newWord=''.join(blank)
    print(newWord)
    print(blank)

    #hungan pic
    print()
    print()
    print("----------------HUNGMAN----------------")
  
    print()
    print("----+-----------")
    print("    |")
    if(life==5):
        print("\n")
        print("\n")
        print("\n")

    elif(life==4):
        print("    0")
        print("\n")
        print("\n")
    elif(life==3):
         print("    0")
         print("    |")
         print("\n")
    elif(life==2):
         print("    0")
         print("   /|\\")
         print("\n")

    elif(life==1):
         print("    0")
         print("   /|\\")
         print("   /")
    else:
         print("    0")
         print("   /|\\")
         print("   / \\")

         print("Hungman died....")

    



print()
print()
if(life>0):
    print("You Won the game!!!")
else:
    print("You loose!!!")

