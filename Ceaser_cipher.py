#e(x)=(X+n)mod 26......--->Encription
#d(x)=(X-n)mod 26......--->Decription
import string


alphabet=string.ascii_lowercase
x=input("Type 'encrypt' fo encription, type 'decrypt' for decription:\n")

msg=input("Type your msg:\n")
n=int(input("Type the shift number:\n"))
if x=='encrypt':
    msg=msg.lower()
    encrypted=''
    for i in range(len(msg)):
        letter=msg[i]
        position=alphabet.index(letter)
        e=position+n
        encrypted+=alphabet[e]
    
        
    res=encrypted
    print(f"Here is the encrypted result:{res}")
else:
    decrypted=''
    for i in range(len(msg)):
        letter=msg[i]
        position=alphabet.index(letter)
        d=position-n
        decrypted+=alphabet[d]
    
        
    res=decrypted
    print(f"Here is the decrypted result:{res}")