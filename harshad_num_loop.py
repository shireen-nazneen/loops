num=int(input("enter your number__"))
copy=num
sum_digit=0
while copy>0:
    digit=copy%10
    sum_digit=sum_digit+digit
    copy=copy//10
if num%sum_digit==0:
    print(num, "its is harshad number")
else:
    print(num, "it is not harshad number")