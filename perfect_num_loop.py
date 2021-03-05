num=int(input("enter number--"))
i=1
while i<=num:
    c=0
    j=0
    while j<=i:
        if num%1==0 and num%num==0:
            c+=1
        j=j+1
    i+=1
if c==2:
    print(num," is a perfect number")
else:
    print(num,"is a not perfect number")