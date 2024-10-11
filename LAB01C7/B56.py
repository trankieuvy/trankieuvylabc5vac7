# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 19:12:34 2024

@author: trankieuvy

"""

import math
def chuvi_dt(hinh,pheptinh, *args,**kwargs):
    if hinh == 'vuong':
        canh = args[0]
        return canh*4 if pheptinh == 'chuvi' else canh**2
    elif hinh == 'chunhat':
        dai = args[0]
        rong = args[1]
        return 2*(dai + rong) if pheptinh == 'chuvi' else dai*rong
    elif hinh == 'hinhtron':
        bk = args[0]
        return 2 * math.pi * bk if pheptinh == 'chuvi' else math.pi * bk**2
    else:
        return 'hinh khong dung'
    
    
#if__name__=="__main__"
print('chu vi hinh vuong:', chuvi_dt('vuong', 'chuvi',5))
print('dien tich hinh vuong: ', chuvi_dt('vuong','dientich',5))
      
print('chu vi hinh chu nhat: ', chuvi_dt('chunhat','chuvi', 5, 4))
print('dien tich hinh chu nhat: ', chuvi_dt('chunhat','dientich', 5, 4))
print('chu vi hinh tron:', chuvi_dt('hinhtron','chuvi', 5))
print('dien tich hinh tron: ',chuvi_dt('hinhtron','dientich',5))
