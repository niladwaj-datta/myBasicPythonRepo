num=int(input("Enter your number"))
a=num
st=str(num)
l=len(st)
sum=0
for i in range(l):
    digit=int(st[i])
    sum+=digit**(i+1)



if sum==num:
    print(f"{num} is a disarium number")
else:
    print(f"{num} is not a disarium number")

