# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:54:55 2024

@author: trankieuvy
"""

def in_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
if __name__== '__main__':   
    print(in_fibonacci(10))
    print("Đã in xong dãy Fibonacci.")
 