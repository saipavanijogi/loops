n=int(input("enter the number"))
temp=n
sum=0
while n>0:
    fact=1
    i=1
    rem=n%10
    while i<=rem:
        fact=fact*i
        i=i+1
        sum=sum+fact
        n=n//10
if sum==temp:
    print("it is a strong number")
else:
    print("it is not a strong number")
      
              