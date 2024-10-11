# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:03:47 2024

@author: trankieuvy

"""
def ktra_giatri():
    gtri = input('Nhp gia tri:')
    #if gtri.replace('.','',1).replace('-','',1).isdigit():
        #gtri = float(gtri)
    #cach 2 kiem tra, ep kieu int()
    #if gtri.lstrip('-').isdigit():
        #gtri = int(gtri)
    #vi du: -12344-, cat dau tru truoc va sau
    if gtri.strip('-').isdigit():
        gtri = int(gtri)
    if -86 <= gtri <= 90:
        return gtri
    print('Hong hop le, nhap lai:')
    return ktra_giatri()


if __name__=="__main__":
    print(ktra_giatri())
                
