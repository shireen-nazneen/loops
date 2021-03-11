num=int(input('enter first number----'))
num1=int(input('enter your scend number-----'))
while num%num1!=0:
    r=num%num1
    num=num1
    num1=r
print("your hcf number is this,",num1)