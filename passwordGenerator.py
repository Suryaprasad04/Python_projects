import random
import string
print("Welcome to the password Generator!")
letters=int(input("How many letters would you like in your password?\n"))
symbol=int(input("How many Symbols would you like in your password?\n"))
num=int(input("How many  numbers would you like in your password?\n"))


password=''
for i in range(letters):
    password+=random.choice(string.ascii_letters)
for j in range(symbol):
    password+=random.choice(string.punctuation)
for k in range(num):
    password+=str(random.randint(0,10))


password_list = list(password)#Convert the password string into a list so the characters can be shuffled
random.shuffle(password_list)#Shuffle the characters in the list randomly to make the password harder to predict.
final_password = ''.join(password_list)#Join the shuffled list back into a string and print the final password.

# Output: Show the generated password
print("Your password is:", final_password)





#(................join function...............)



# Joining a List with No Separator

# characters = ['A', 'b', 'c', '1', '2']
# joined_string = ''.join(characters)
# print(joined_string)  # Output: "Abc12"
