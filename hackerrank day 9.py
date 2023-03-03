import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    if n==0:
        return 1
    else:
        fact=1
        for i in range(1,n+1):
           fact=fact*i 
        return fact
     
    

if __name__ == '__main__':

    n = int(input("Enter the number:").strip())

    result = factorial(n)
    print("Factorial:",result)
