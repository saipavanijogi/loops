# EDCBA
# EDCB
# EDC
# ED
# E

n=int(input("enter the number"))
i=0
while i<=n:
    k=ord("E")
    j=1
    while j<=n-i:    
        print(chr(k),end="")
        k=k-1
        j=j+1
    print()
    i=i+1