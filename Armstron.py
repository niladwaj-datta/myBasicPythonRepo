num=int(input("Enter your number"))
a=num
exp=3
sum=0
mes1=f"{num} is an armstrong number"
mes2=f"{num} is not an armstrong number"
isarm=False
while a>0 :
    rem=a%10
    sum+=rem**exp
    a//=10



if num==sum:
    isarm=True


if isarm:
        print(mes1)
else:
        print(mes2)