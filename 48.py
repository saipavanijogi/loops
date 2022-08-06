    #     1
    #    21 
    #   321
    #  4321 
    # 54321  
      
n=int(input("enter the number"))
i=1
while i<=5:
    j=0
    while j<=5-i:
        print(" ",end="")
        j=j+1
    j=0
    while j<i:
        print(i-j,end="")
        j=j+1
    print()
    i=i+1

#1
#234
#56789
num=1  
i=0
while i<=5:
  j=0
  while j<=i:   
      print(num,end=" ")
      num+=1
      j=j+1
  print()
  i=i+2 
 
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

# *
# **
# ***
# ****
# *****       
        
n=int(input("enter the number"))     
i=1
while i<=n:
  j=1
  while j<=i:
      print("*",end='')
      j=j+1
  print()
  i=i+1

#     *
#    * *
#   * * *
#  * * * *
# * * * * *        
         
n=int(input("enter the number"))
i=1
while i<=n:
   j=1
   while j<=n-i:
     print(" ",end=" ")
     j=j+1
   j=1 
   while j<=i:
     print("*",end="   ")
     j=j+1
   print()
   i=i+1



n=int(input("enter the number"))
i=1
while i<=n:
  j=1
  while j<=n:
    print(j,end="")
    j=j+1
  print()
i=i+1
  
# A1  
# A1 B2
# A1 B2 C3
# A1 B2 C3 D4
# A1 B2 C3 D4 E5

i=65
while i<=69:
  k=1
  j=65
  while j<=i:
     print(chr(j),k,end=" ")
     k=k+1
     j=j+1
  print()
  i=i+1

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



