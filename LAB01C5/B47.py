# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:10:48 2024

@author: Admin
"""
#BÀI 47

danhsach=[]
max=0

for x in range (1,490):
    for y in range (1,140):
        for z in range (1,109):
            if 2*x + 7*y + 9*z == 979:
                sum = x+y+z
                if sum > max:
                    max = sum
                    danhsach=[(x,y,z)]
            
print(f"{danhsach} với bộ nghiệm (x+y+z)={max}")