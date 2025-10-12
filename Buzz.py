from operator import truediv

num=int(input("Enter your number:"))
a=num
isbuzz=False
rem=a%10
div=a%7
if rem==7 or div==0:
          isbuzz=True








if isbuzz:
    print(f"{num}  is a buzz number")
else:
    print(f"{num} is not a buzz number")