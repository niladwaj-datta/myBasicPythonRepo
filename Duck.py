num=int(input("Enter your number:"))
a=num
isduck=False
while a>0:
    rem=a%10
    if rem==0:
         isduck=True
         break
    else:
         a//=10








if isduck:
    print(f"{num} is a duck number")
else:
    print(f"{num} is not a duck number")
