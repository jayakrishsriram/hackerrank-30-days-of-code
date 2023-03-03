import math
import os
import random
import re
import sys


#reversing the input order
if __name__ == '__main__':
    n = int(input("Enter the Number of input:").strip())

    arr = list(map(int, input("Enter the input:").rstrip().split()))
    rev=[]
    for i in range(n):
        rev.append(arr[n-i-1])
    out=''
    for i in  range(len(rev)):
       out+=str(rev[i])+' '
    print(out)   
