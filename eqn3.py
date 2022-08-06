num=int(input("enter the number"))
i=2
sum=0
a=num%2
while i<=a:
    if num%i==0:
        sum=1
        break
    i=i+1
if num==sum:
    print("it is prime number")
else:
    print("not a prime")
    




