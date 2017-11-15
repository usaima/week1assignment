# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 20:47:34 2017

@author: OPS
"""
import math

def magni(v1):
    
    tmp1 = v1[0]**2 +  v1[1]**2
    result = math.sqrt(tmp1)
        
    return result

a = [1,2]

print("Magnitude: ",magni(a))