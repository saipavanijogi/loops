
#   1
#   21
#   321
#   4321
#   54321
  
n=int(input("enter the number"))  
i=1
while i<=n:
    j=0
    while j<i:
        print(i-j,end="")
        j=j+1
    print()
    i=i+1



