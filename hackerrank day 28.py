import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    firstNameList=[]
    pattern=r"@gmail\.com$"
    regex=re.compile(pattern)
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        if regex.search(emailID):
            firstNameList.append(firstName)
    firstNameList.sort()    
    for name in firstNameList:
        print(name) 
