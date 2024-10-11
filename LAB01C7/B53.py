# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:22:15 2024

@author: trankieuvy
"""

import math

def tong_tu_1_den_n(n):
    return sum(range(1, n + 1))

def tong_binh_phuong_tu_1_den_n(n):
    return sum(i**2 for i in range(1, n + 1))

def tong_phan_so_tu_1_den_n(n):
    return sum(1/i for i in range(1, n + 1))

def tong_giai_thua_tu_1_den_n(n):
    return sum(math.factorial(i) for i in range(1, n + 1))

def tich_tu_1_den_n(n):
    tich = 1
    for i in range(1, n + 1):
        tich *= i
    return tich

if __name__== '__main__':   
    print(tong_binh_phuong_tu_1_den_n(5))
    print(tong_binh_phuong_tu_1_den_n(6))
    print(tong_phan_so_tu_1_den_n(8))
    print(tong_giai_thua_tu_1_den_n(4))
    print(tich_tu_1_den_n(9))
    