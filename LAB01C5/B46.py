# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:53:47 2024

@author: trankieuvy
"""
#BÀI 46

danhsach=[]

for x in range (1,490):
    for y in range (1,140):
        for z in range (1,109):
            if 2*x + 7*y + 9*z == 979:
                danhsach+=[(x,y,z)]
for i in danhsach:
    print("Bộ nghiệm",i)
   
#Kiểm tra điều kiện của x,y,z
while x<=0 and y<=0 and z<=0:
    print("không hợp lệ")


    