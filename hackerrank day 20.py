
import math
import os
import random
import re
import sys



n = int(input().strip())
a = list(map(int, input().rstrip().split()))
# Write your code here
t_s=0
for i in range(n):
    n_s=0
    for j in range(n-1):
        if a[j]>a[j+1]:
           tmp=a[j]
           a[j]=a[j+1]
           a[j+1]=tmp
           n_s+= 1
    t_s+=n_s       
    if n_s ==0:
        break       
print('Array is sorted in '+str(t_s)+' swaps.')
print('First Element: '+str(a[0]))
print('Last Element: '+str(a[n-1]))  
