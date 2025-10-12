num=int(input("Enter your number:"))
a=num
sum1=0
sum2=0
while a>0:
    rem1=a%10
    sum1+=rem1**2
    a//=10




b=sum1
while b>0:
    rem2=b%10
    sum2+=rem2**2
    b//=10



if sum2==1:
    print(f"{num} is a happy number")
else:
    print(f"{num} is not a happy number")
