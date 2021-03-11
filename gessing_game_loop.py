my_number=5
i=0
counter=5
while i<=5:
    if i==5:
        print("this is your last chance")
    user=int(input("enter your number"))
    if user==my_number:
        print("your answer is correct")
        break
    else:
        print("wrong try again")
    i=i+1