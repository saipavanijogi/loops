# 11111
# *****
#  333
#  * *
#   5

i=1
while i<=5:
    j=0
    while j<=5-i:
        if i%2==0:
            print("*",end=" ")
        else:
            print(i,end=" ")
        j+=1
    print()
    i+=1

    