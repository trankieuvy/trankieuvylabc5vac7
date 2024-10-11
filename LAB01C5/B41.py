# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:33:14 2024

@author: trankieuvy
"""

n=int(input("Nhập  số n: "))
S=0
while n<=0:
    n=int(input("Nhập lại n:"))
    
for i in range (1,n+1):
    S+=1/(2*i+1)
print("Tổng S=1+1/3+1/5+...+1/2n+1 là :",S)