n=int(input("enter the number"))
i=1
while i<=n:
  j=1
  while j<=n:
    print(j,end="")
    j=j+1
  print()
i=i+1
  
 # out put 1,2,3,4,5,6,*,*,*,10 
i=1
while i<=10:
    if i>=6 and i<=9:
        print("*")
    else:
        print(i)
    i+=1