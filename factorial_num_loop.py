num=int(input("enter number:    "))
copy=num
i=1
m=0
sum1=1
while i<=num:
    if num%i==0:
        m=num
        print(i,"is a factror of ",num) 
        sum1=sum1*i
    i=i+1
print(sum1)