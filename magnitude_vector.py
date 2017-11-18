# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 20:47:34 2017

@author: OPS
"""
import math

def magni(v1):
    
    tmp1 = 0
    for i in range(len(v1)):
        tmp1 = tmp1 + v1[i]**2
    result = math.sqrt(tmp1)
        
    return result

a = [1,2,3]

print("Magnitude: ",magni(a))