num=int(input("Enter your number"))
a=num
pal=0
mes1=f"{num} is a palindrome number"
mes2=f"{num} is not a palindrome number"
while a>0:
    b=a%10
    pal=pal*10+b
    a//=10


if num==pal:
    print(mes1)
else:
    print(mes2)
