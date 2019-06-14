# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 04:02:09 2019

@author: Ju
"""


import numpy as np

list1=np.loadtxt('IntegerArray.txt',delimiter='\n')


def Sort_and_CountInv(A):
    n=len(A)

    if n==0 or n==1:
        return(A,0)
    else:
        list_left=A[:int(n/2)]
        list_right=A[int(n/2):]
        (C,leftInv)=Sort_and_CountInv(list_left)
        (D,rightInv)=Sort_and_CountInv(list_right)
        (B,splitInv)=Merge_and_CountSplitInv(C,D)
        return (B,leftInv+rightInv+splitInv)

def Merge_and_CountSplitInv(C,D):
    i=0
    j=0
    splitInv=0
    B=np.zeros(len(C)+len(D))
    len1=len(C)+len(D)
    for k in range(len1):
       if C[i] <D[j]:
           B[k]=C[i]
           if i==(len(C)-1):
               B[k+1:]=D[j:]
               break
           else: 
               i=i+1
       else:
           B[k]=D[j]
           splitInv=splitInv+len(C)-i
           if j==(len(D)-1):
               B[k+1:]=C[i:]
               break
           else:
               j=j+1
    return (B,splitInv)

print(Sort_and_CountInv(list1))
