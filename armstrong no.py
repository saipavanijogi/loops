n=int(input("enter the number"))
length=len(str(n))
temp=n
sum=0
while temp!=0:
    digit=temp%10
    sum=digit**10
    temp=temp//10
if sum==temp:
    print("strong number")
else:
    print("not a strong number")
    
    