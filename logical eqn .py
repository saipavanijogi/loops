i=1
while i<=11:
    j=1
    while j<=11:
        if  j==1 or j==11 or i==1 or i==11:
            print("p",end=" ")
        elif j==2 or j==10 or i==2 or i==10:
            print("a",end=" ")
        elif  j==3 or j==9 or i==3 or i==9:
            print("v",end=" ")
        elif  j==4 or j==8 or i==4 or i==8 :
            print("a",end=" ")
        elif j==5 or j==7 or i==5 or i==7:
            print("n",end=" ")
        elif i==j==6:
            print("i",end=" ")
        j+=1
    print()
    i+=1

