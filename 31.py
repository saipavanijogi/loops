# 1
# 2*
# 3*3*
# 4*4*4*
# 5*5*5*5

n=int(input("enter the number"))
i=1
while i<=n:
    j=1 
    while j<=i:
        if j%2!=0:
            print(i,end="")
        else:
            print("*",end="")
        j=j+1
    print()
    i=i+1

