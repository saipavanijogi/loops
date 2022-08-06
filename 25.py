def function(a,p):
    for i in range (a,p):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
a=int(input( "number "))
p=int(input("enter "))
function(a,p)

