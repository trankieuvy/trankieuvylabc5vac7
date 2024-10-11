# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:42:12 2024

@author: Admin
"""

n=int(input("Nhập  số n: "))
S=0
while n <= 0:
    n=int(input("Nhập lại số n: "))
for i in range (1,n+1):
    S+=i/(i+1)
print("Tổng S=1/2+1/3+...+n/n+1 là: ",S)