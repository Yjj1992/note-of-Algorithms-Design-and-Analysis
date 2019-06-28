# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 23:18:35 2019

设有一个adjacency list，第一列为标号为1到200的顶点，其余列为每一个顶点连接的点
设计随机收缩算法，求上述无向图的min cut

@author: Ju
"""
import random as rd
import numpy as np

#A=np.loadtxt('kargerMinCut.test.txt',delimiter='\n')
#print(A)

data_temp=[]
with open('kargerMinCut.txt') as fdata:
        while True:
            line=fdata.readline()
            if not line:
                break
            data_temp.append(np.array([int(i) for i in line.split()]))
A=np.array(data_temp)


def Random_Contraction(A):
    i=A.shape[0]
    CE=0
    while i>2:
        j=rd.randint(0,A.shape[0]-1)

        k=rd.randint(0,A[j].shape[0]-1)

        if A[j][0]==A[j][k]:
            continue
        else:
            temp=A[j][0]
            temp1=A[j][k]
            for m in range(A.shape[0]):
                for n in range(A[m].shape[0]):
                    if A[m][n]==temp1:
                        A[m][n]=temp
            i=i-1
    for p in range(A.shape[0]):
        for q in range(A[p].shape[0]):
            if A[p][0]!=A[p][q]:
                CE=CE+1
    CE=CE/2
    return CE
print(Random_Contraction(A))
