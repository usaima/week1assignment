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

def unit(vec,mag):
    uv = []
    for i in range(len(vec)):
        uv.append(vec[i] / mag)
    return uv

a = [1,2,3]
m = magni(a)
u = unit(a,m)
print("Magnitude: ",m)
print("Unit Vector ",u)
