n = int(input("Enter the number:").strip())
c=0
m=0
d=bin(n)
print("Binary Number of ",n," is ",d)
while n > 0:
    r = n % 2
    if r==1:
       c+=1
       if c>m:
            m=c
    else:
        c=0
    n=n//2
print(" maximum Number of 1 repeating next to next")
print(m)      
