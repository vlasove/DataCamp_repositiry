def add(a,b):
    print( a+b)
    
    

def isTriangle(A,B,C):
    if A**2 + B**2 == C**2 or B**2 + C**2 == A**2 or C**2 + A**2 == B**2 :
        return True 
    return False


c = 0
for i in range(0,50):
    for j in range(0,50):
        for k in range(0,50):
            if isTriangle(i,j,k):
                print(i,j,k)
                c+=1

print(c)
