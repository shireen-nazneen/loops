num=int(input("enter your number---"))
i=1
copy=num
sum_num=0
while i<num:
    if num%i==0:
        sum_num=sum_num+i
    i=i+1
if sum_num==num:
    print(num,"this is perfect number")
else:
    print(num,"this is not perfect number")

