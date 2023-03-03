import sys
n=int(input("Enter the number of input:").strip())
phone_book={}
for i in range(n):
    e=input().split(' ')
    phone_book[e[0]]=e[1]
q=sys.stdin.readline().strip()
while q:
    p_no=phone_book.get(q)
    if p_no:
        print(q+'='+p_no)
    else:
        print('Not found')
    q=sys.stdin.readline().strip()       
'''
input:
sam 99922
tom 11234
harry 12334
sam
ed
harry
output:
sam=99922
not found
harry=12334
'''
