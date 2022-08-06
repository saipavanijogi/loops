i=1
while i<=5:
  j=1
  while j<=7:
    if i==1 or i==5 or j==1 or j==7:
      print("*",end=" ")
    else:
      print(" ",end=" ")   
    j=j+1
  print()
  i=i+1



