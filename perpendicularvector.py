# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:25:36 2017

@author: OPS
"""

def dot(v1,v2):
    result = 0
    for i in range (len(v1)):
        result = result + (v1[i] * v2[i])
        
    return result

a = [1,-2,3]
b = [5, 4,1]

dp = dot(a,b)
print ("dot product of a and b is ",dp)
if(dp==0):
    print("a and b are perpendicular")
elif(dp==1 or dp == -1):
    print ("a and b are parallel")
