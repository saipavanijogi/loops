#print("\UOOO1F637")
def function(n,m):
    for i in range(n,m):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i,end="")
n=int(input("enter the number"))
m=int(input("enter the number"))
function(n,m)
        
        
    
           
   
    
    
    
    
   