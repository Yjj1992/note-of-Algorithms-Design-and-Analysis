# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:36:55 2019

@author: Ju
"""

def m_Karatsuba(x,y):
    x_str=str(x)
    y_str=str(y)
    m=len(x_str)
    m=int(m)
    if m==1:
        result=x*y
    else:
        a=int(x_str[:int(m/2-1)])
        b=int(x_str[int(m/2):])
        c=int(y_str[:int(m/2-1)])
        d=int(y_str[int(m/2):])
        p=a+b
        q=c+d
        ac=a*c
        bd=b*d
        abdc=p*q-ac-bd
        result=10**m*ac+10**(m/2)*abdc+bd
    return result

print(m_Karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
        
        
        
    