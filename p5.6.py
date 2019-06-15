# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 08:32:58 2019
问题5.6 实现QuickSort算法，通过跟踪特征值（如比较次数）的方法比较下列三种选取支点的方法那种更优秀
1）总选第一个元素作为支点
2）总选最后一个元素作为支点
3）使用随机选取支点的方式（此方法需要连续针对输入数组运算10次，并计算出比较次数的平均值）
4）使用位置在第一个，最后一个以及位置在中间的三个数值中处于中间的数值作为支点

@author: Ju
"""
import numpy as np
import random as rd

A=np.loadtxt('problem5.6.txt',delimiter='\n')

#"""
def CT_of_QS_of_first(A,l,r,CT):
    if l>=r:
        return (A,CT)
    else:
        #下面的代码将首元素下标作为支点指标
        i=l
        A[np.array([l,i])]=A[np.array([i,l])]
        (A,j,CT1)=Partition(A,l,r,CT)
        (A,CT2)=CT_of_QS_of_first(A,l,j-1,CT1)
        (A,CT3)=CT_of_QS_of_first(A,j+1,r,CT2)
        return (A,CT3)
        
print(CT_of_QS_of_first(A,0,(A.shape[0]-1),0))   
#"""    

"""  
def CT_of_QS_of_last(A,l,r,CT):
    if l>=r:
        return (A,CT)
    else:
        #下面的代码将最后元素下标作为支点指标
        i=r
        A[np.array([l,i])]=A[np.array([i,l])]
        (A,j,CT1)=Partition(A,l,r,CT)
        (A,CT2)=CT_of_QS_of_last(A,l,j-1,CT1)
        (A,CT3)=CT_of_QS_of_last(A,j+1,r,CT2)
        return (A,CT3)    

print(CT_of_QS_of_last(A,0,(A.shape[0]-1),0))  
"""

"""
def CT_of_QS_of_random(A,l,r,CT):
    if l>=r:
        return (A,CT)
    else:
        #下面的代码将随机下标作为支点指标
        i=rd.randint(l,r)
        A[np.array([l,i])]=A[np.array([i,l])]
        (A,j,CT1)=Partition(A,l,r,CT)
        (A,CT2)=CT_of_QS_of_random(A,l,j-1,CT1)
        (A,CT3)=CT_of_QS_of_random(A,j+1,r,CT2)
        return (A,CT3)   

#下方程序用于计算10次随机取点QS算法的比较次数平均值
def Averge_of_CT_of_randomQS(A):
    CT_All=0
    for m in range(10):
        A_temp=A
        B=CT_of_QS_of_random(A_temp,0,(A_temp.shape[0]-1),0)
        CT_All=CT_All+B[1]
    return CT_All/10
    
print(Averge_of_CT_of_randomQS(A))

"""
"""
def CT_of_QS_of_medianThree(A,l,r,CT):
    if l>=r:
        return (A,CT) 
    elif r-l==1:
        if A[l]>A[r]:
            A[np.array([l,r])]=A[np.array([r,l])]
        return (A,CT+1)
    else:
        #下面的代码将首元素,尾元素以及中间元素三者中中间值的下标作为支点指标
        if A[l]<=A[r]:
            if A[l]>A[l+int((r-l)/2)]:
                i=l
            elif A[l+int((r-l)/2)]<=A[r]:
                i=l+int((r-l)/2)
            else:
                i=r            
        elif A[r]<=A[l+int((r-l)/2)]:
            if A[l]<=A[l+int((r-l)/2)]:
                i=l
            else:
                i=l+int((r-l)/2)
        else:
            i=r
        A[np.array([l,i])]=A[np.array([i,l])]
        (A,j,CT1)=Partition(A,l,r,CT)
        (A,CT2)=CT_of_QS_of_medianThree(A,l,j-1,CT1)
        (A,CT3)=CT_of_QS_of_medianThree(A,j+1,r,CT2)
        return (A,CT3)  
print(CT_of_QS_of_medianThree(A,0,(A.shape[0]-1),0))
""" 
    
def Partition(A,l,r,CT):
    p=A[l]
    i=l+1
    for j in np.arange(l+1,r+1,1):
        if A[j]<p:
            A[np.array([i,j])]=A[np.array([j,i])]
            i=i+1
        CT=CT+1
    A[np.array([l,i-1])]=A[np.array([i-1,l])]
    return (A,i-1,CT)




