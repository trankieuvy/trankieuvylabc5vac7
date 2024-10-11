# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:58:29 2024

@author: trankieuvy
"""

def tinh_chu_vi(dai, rong):
    return 2 * (dai + rong)

def tinh_dien_tich(dai, rong):
    return dai * rong

def ve_hinh_chu_nhat(dai, rong):
    for i in range(rong):
        print('*' * dai)
if __name__== '__main__':   
    print(tinh_chu_vi(5, 3))
    print(tinh_dien_tich(5, 3))
    print(ve_hinh_chu_nhat(5, 3))
    