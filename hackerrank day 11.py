import math
import os
import random
import re
import sys
'''#This program is to find hourglass sum
#hourglass meaning:
eg:
1 1 1 0 0
1 2 0 1 0
2 3 1 0 0
1 0 1 0 1
1 0 0 0 1

Now when we consider the given value we must consider like this

a11 a12 a13
    a22
a31 a32 a33

seeing all the posible way we must check for maximum sum possible way. 
'''
if __name__ == '__main__':

    arr = []
    print("Enter the 6 number for 6 lines")
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
a=-2**31 
for i in range(4):
        for j in range(4):
            q=arr[i][j]
            q+=arr[i][j+1]
            q+=arr[i][j+2]
            q+=arr[i+1][j+1]
            q+=arr[i+2][j]
            q+=arr[i+2][j+1]
            q+=arr[i+2][j+2]
            if a<q:
                a=q
print(a)            
