class Difference:
    def __init__(self, a):
        self.__elements = a
        
        self.maximumDifference = 0
    def computeDifference(self):
        min_element=101
        max_element=0
        for element in self.__elements:
           if element < min_element:
             min_element = element
           if element > max_element :
             max_element = element       
        self.maximumDifference= max_element-min_element
'''
first:
input: 1 2 5   input is stored as[1,2,5]
goes to class
maxdiff=0
min_element=101
max_element=0
using for loop -1),2),3)-indicates no of loop
1)
1<101
min_ele=1
1>0
max_ele=1
maxdiff=max-min=1-1=0
2)
2<1 false
min_ele=1
2>1
max_ele=2
maxdiff=max-min=2-1=1
now maxdiff is stored as 1
3)
5<1 false
min_ele=1
5>2
max_ele=5
maxdiff=5-1=4
and maxdiff is returned as output
'''

a = [int(e) for e in input("Enter the numbers:").split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)        
