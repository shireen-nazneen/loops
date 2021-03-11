num=int(input("enter your number_--"))
counter=0
i=1
while i<=num:
    if num%i==0:
        counter+=1
    i=i+1
if counter==2:
    print(num,"is prime number")
else:
    print(num, 'is not prime number')