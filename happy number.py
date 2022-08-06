n=int(input("enter the number"))
temp=n
sum=0 
while sum!=1 and sum!=4:
    sum=0
    while temp!=0:
        rem=temp%10
        sum=sum+rem*rem
        temp=temp//10
    temp=sum
if sum==1:
   print("it is a happy number")
else:
   print("it is a un happy number")
    
      
              



      