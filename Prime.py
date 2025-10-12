num=int(input("Enter your number"))
a=int(num/2)
isprime=True
mes1=f"{num} is a prime number"
mes2=f"{num} is not a prime number"
if(num<2) :
    isprime=True
else:
 for i in range(2,a+1):
    if num%i==0:
        isprime=False
        break


if isprime:
    print(mes1)
else:
    print(mes2)