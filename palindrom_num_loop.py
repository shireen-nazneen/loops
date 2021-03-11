num=int(input("enter your number"))
r=0
s=num
while num>0:
    r=(r*10)+num%10
    num=num//10
if s==r:
    print(r,"is palindrome number number")
else: 
    print(r,"is  it not pslindrome number")