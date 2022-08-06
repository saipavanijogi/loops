
# EDCBA
# DEBA
# CBA
# BA 
# A

n=5
i=0
while i<=n:
    k=ord("E")-i
    j=1
    while j<=n-i:
      print(chr(k),end="")
      k=k-1
      j=j+1
    print()
    i=i                                                                                       +1

