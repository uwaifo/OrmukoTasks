'''Question B
The goal of this question is to write a software library that accepts 2 version string as input 
and returns whether one is greater than, equal, or less than the other. 
As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
 
'''
#SOLUTION
import re

def add(x,y):
    return x + y


def greaterString(str_1,str_2):

    #extrant numeric value from each string argument
    num_1 = re.findall('\d*\.?\d+',str_1)
    num_2 = re.findall('\d*\.?\d+',str_2)


    if len(num_1) == 1 and len(num_2) == 1:
        if num_1[0] > num_2[0]:
            try:
                return int(num_1[0])
            except ValueError:
                return float(num_1[0])
        if num_2[0] > num_1[0]:
            try:
                return int(num_2[0])
            except ValueError:
                return float(num_2[0])
            
    elif len(num_1) == 0 or len(num_2) == 0:
         return "Invalid entry: One or both of your string arguments has no numeric values"  
    else:
        return "Invalid entry: One or both of your string arguments has multiple numeric values"


# TESTS
'''
print(greaterString("1.2","1.1"))
print(greaterString("2.1", "2.11"))
print(greaterString("2.1", "two"))
print(greaterString("1.2 4", "2.11"))
'''

 

