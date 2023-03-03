t=int(input("Enter the number of input:"))
#splits even and odd position of the word 
for i in range(t):
    s=input("Enter the word:")
    d=len(s)
    a=''
    b=''
    for j in range(0,d):
        if j%2==0:
            a+=s[j]
        else:
            b+=s[j]
    print(a+' '+b) 
'''
input:
  2
  hacker
  rank
output:
  hce akr
  rn ak
'''  
