a=int(input("enter number"))
i=a
sum=0
c=len(str(a))
while i>0:
    d=i%10
    sum=sum+d**c
    i=i//10
print(sum)
if a==sum:
    print(a,"amstrong number")
else:
    print(a,"this is not amstrong number")