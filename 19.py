    
#  A
#  AB
#  ABC
#  ABCD
#  ABCDE 
    
n=int(input("enter the number"))
i=1
while i<=n:
    k=ord("A")
    j=1
    while j<=i:    
        print(chr(k),end="")
        k=k+1
        j=j+1
    print()
    i=i+1
    