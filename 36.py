#o/p 5 5 5 5 5
   # 4 4 4 4 
   # 3 3 3 
   #2 2 
   # 1
    
n=int(input("enter the number"))
i=0
while i<=n:
    j=n
    while j>i:
        print(n-i,end="")
        j=j-1
    print()
    i=i+1

