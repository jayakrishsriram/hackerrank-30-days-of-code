import math

def prime(n):
    if n<=1:
        return False
    f=math.sqrt(n)
    if f.is_integer():
        return False
    for i in range(2,int(f) +1):
        if n%i==0:
            return False
    return True    

a=int(input())
for i in range(a):
    n=int(input())
    if prime(n):
        print('Prime')
    else:
        print('Not prime')    
