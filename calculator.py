def opt(f):
    s=int(input("Enter second number:"))
    op=input("Enter you opreration:")

    operation={
        '+':f+s,
        '-':f-s,
        '*':f*s,
        '/':f/s
    }
    # I am confident that the user will enter a valid operator, so I am not handling the case of invalid operator here.
    print(f"{f} {op} {s} = {operation[op]}")


f=int(input("Enter first number:"))
opt(f)
while(True):
    uinput=input(f"Enter 'y' to continue calculation with first number {f}\nEnter 'n' to give other inputs\nEnter x to exit\n"  )

    if(uinput=='y'):
        opt(f)
    elif(uinput=='n'):
        f=int(input("Enter first number"))
        opt(f)
    elif(uinput=='x'):
        break
exit
          