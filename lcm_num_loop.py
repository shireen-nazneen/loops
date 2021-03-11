num_1=int(input("enter your number"))
num_2=int(input("enter your number"))
if num_1>num_2:
    max_num=num_1
else:
    max_num=num_2
while 1:
    if max_num%num_1==0 and max_num%num_2==0:
        print(num_1,num_2,"lcm of these number is ", max_num)
        break
    max_num+=1
