n=int(input("enter the number"))
temp=0
sum=0
while temp!=0:
    rem=temp%10
    sum=(sum*10)+rem
    temp=temp//10
    print(sum)
if sum==temp:
    print("it is a paliondra")
else:
    print("it is not a paliondra")
    
    