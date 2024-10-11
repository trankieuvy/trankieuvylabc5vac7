# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:35:18 2024

@author: trankieuvy

"""

import math


#Phương thức tính căn bậc x của số n
def canbac_x(n,x):
    return n**(1/x)

#b) Phương thức trả về số đảo.
def so_dao(n):
    return int(str(n)[::-1])

#c) Phương thức kiểm tra có phải là số chính phương.
def so_chinh_phuong(n):
    return math.sqrt(n)==int(math.sqrt(n))


#d) Phương thức kiểm tra có phải là số nguyên tố

def so_nguyen_to(n):
    if n<2:
        return False
    for i in range (2,n):
        if n%i == 0:
            return False
    return True

#e) Phương thức tính tích các chữ số lẻ.

def tichsole(n):
    tich=1
    for i in str(n): 
        if int(i)%2 != 0:
             tich *= int(i)
        return tich
    
#f) Phương thức tính tổng các số nguyên tố nhỏ hơn n
def tong_ngto_nho_n(n):
    tong_ngto = 0
    for i in range(2, n):
        if so_nguyen_to(i):
            tong_ngto += i
    return tong_ngto

#g) Phương thức tính tổng các số chính phương nhỏ hơn n.
def tong_chinhphuong(n):
    tong_cp = 0
    for i in range (1, int(math.sqrt(n))+1):
        tong_cp += i**i
        return tong_cp

#h) Phương thức tính tổng các ước số dương của n

def tong_uoc_so(n):
    tong = 0
    for i in range(1, n + 1): 
        if n % i == 0: 
            tong += i
    return tong
    
if __name__== '__main__':   
    print(canbac_x(8,3))
    print(so_dao(123450))
    print(so_chinh_phuong(9))
    print(so_nguyen_to(3))
    print(tichsole(3))
    print(tong_ngto_nho_n(7))
    print(tong_chinhphuong(9))
    print(tong_uoc_so(6))
    
