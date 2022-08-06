# A
# BA
# CBA
# DCBA
# EDEBA

n=5
i=0
while i<n:
     k=ord("A")+i
     j=0
     while j<=i:    
        print(chr(k),end="")
        k=k-1
        j=j+1
     print()
     i=i+1
 