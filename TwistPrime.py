num=int(input("Enter your number:"))
a=num
b=num
pal=0
isnum=True
ispal=True
while a>0:
    rem=a%10
    pal=pal*10+rem
    a//=10


r=int(num/2)
for i in range(2,r+1):
      rem1=b%i
      if rem1==0:
            isnum=False





c=pal
s=int(pal/2)
for i in range(2,s+1):
    rem2=c%i
    if rem2==0:
        ispal=False









if isnum and ispal:
    print(f"{num} is not a twisted prime number")
else:
    print(f"{num} is  a  twisted prime number")








