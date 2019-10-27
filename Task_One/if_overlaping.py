'''
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the
x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5)
and (6,8).
'''

def ifOverlaping(x1,x2,x3,x4):
    if x2 > x3:
        return "Overlaping"
    else:
        return "Non-Overlaping"
 

 




