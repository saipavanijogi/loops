# *****
# ****
# ***
# **
# * 

n=int(input("enter the number"))     
i=0
while i<=n:
  j=n
  while j>=n-i:
      print("*",end='')
      j=j-1
  print()
  i=i+1

