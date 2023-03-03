import math
import os
import random
import re
import sys
'''
Task:
Given set S={1,2,3,...,N}. Find two integers, A and B (where A<B), from set S such that the value of A&B is the maximum possible and also less than a given integer,K . In this case,& represents the bitwise AND operator.

Function Description:
Complete the bitwiseAnd function in the editor below.

bitwiseAnd has the following paramter(s):
- int N: the maximum integer to consider
- int K: the limit of the result, inclusive

Returns:
- int: the maximum value of A&B within the limit.

Input Format:

The first line contains an integer,T, the number of test cases.
Each of the  subsequent lines defines a test case as 2 space-separated integers, N and K, respectively.

Constraints
1<=T<=10^3
2<=N<=10^3
2<=K<=N
SAMPLE INPUT:
3
5 2
8 5
2 2
OUTPUT:
1
4
0
#THIS OUTPUT IS WRITTEN IN A TEXT FILE.
'''
#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(n, k):
    # Write your code here
    maximum=0
    for i in range(1,n+1):
        for j in range(1,i):
            h=i & j
            if maximum<h< k:
                maximum=h
            if maximum==k-1:
                return maximum    
    return maximum
    
fptr = open("XYZ.txt", 'w')

t = int(input().strip())

for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

fptr.close()
