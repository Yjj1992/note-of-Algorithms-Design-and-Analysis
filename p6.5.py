# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 03:32:40 2019
问题6.5实现RSelect算法，使用问题5.6中合适的partition算法

@author: Ju
"""

import numpy as np
import random as rd

A=np.loadtxt('problem6.5test2.txt',delimiter='\n')

median=int(len(A)/2)-1

def RSelect(A,m,l,r):
    if l==r:
        return A[0]
    else:
        i=rd.randint(l,r)
        A[np.array([l,i])]=A[np.array([i,l])]
        (A,j)=Partition(A,l,r)
        if j==m:
            return A[j]
        elif j>m:
            return RSelect(A,m,l,j-1)
        else:
            return RSelect(A,m,j+1,r)
        
        
        
def Partition(A,l,r):
    p=A[l]
    i=l+1
    for j in np.arange(l+1,r+1,1):
        if A[j]<p:
            A[np.array([i,j])]=A[np.array([j,i])]
            i=i+1
    A[np.array([l,i-1])]=A[np.array([i-1,l])]
    return (A,i-1)

print(RSelect(A,median,0,len(A)-1))