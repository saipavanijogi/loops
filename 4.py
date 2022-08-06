# ABCDE
# ABCD
# ABC
# AB
# A
   
n=int(input("enter the number"))
i=0
while i<=n:
    k=ord("A")
    j=1
    while j<=5-i:    
        print(chr(k),end="")
        k=k+1
        j=j+1
    print()
    i=i+1