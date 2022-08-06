i=int(input("enter the number"))
n=2
sum=1
while i<=n//2:
    if n%i==0:
       sum+=i
    i=i+1
if sum==n:
    print("it is prefect number")
else:
    print("is not precfect number")
