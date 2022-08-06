num=int(input("enter the number"))
temp=num
sum=0
while temp>0:
     rem=temp%10                    
     sum=sum+rem
     temp=temp//10
if num%rem==0:
    print("it is a harshad number")
else:
    print("it is not harshad number")
