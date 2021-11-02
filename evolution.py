from random import randrange as rnd
import numpy as np


def aproximation():
    n = 60
    pops = []
    mean = [0 for i in range(n)]
    for i in range(n):
        pops.append([rnd(0, 2) for i in range(lenth)])    
    pops_clone = pops.copy()
    for i in range(10000):
        alpha = turnir(pops)[0]
        betta = turnir(pops)[1]
        #gamma = turnir(pops)[2]
        for l in range(2 * n // 3, n):
            pops[l] = pops[l - 2 * n // 3].copy()        
        genetic(alpha)
        genetic(betta)
        for l in range(n // 3):
            pops[l] = alpha[l].copy()
        for l in range(n // 3, 2 * n // 3):
            pops[l] = betta[l - n // 3].copy()   
    return winner(pops)
            
    

    
def func(x):
    s = 0
    for i in range(lenth):
        s = s + x[i] * (-1) ** (i + 1)
    return s


def turnir(x):
    alpha = [0 for i in range(len(x) // 3)]
    betta = [0 for i in range(len(x) // 3)]
    gamma = [0 for i in range(len(x) // 3)]
    x_copy = x.copy()
    for i in range(len(x) // 3):
        a = x_copy.pop(rnd(0, len(x_copy)))
        b = x_copy.pop(rnd(0, len(x_copy)))
        c = x_copy.pop(rnd(0, len(x_copy)))
        d = [a, b, c]
        m_a = func(a)
        m_b = func(b)
        m_c = func(c)
        mean = mean3(m_a, m_b, m_c)
        alpha[i] = d[mean[0]]
        betta[i] = d[mean[1]]
        gamma[i] = d[mean[2]]
    return [alpha, betta, gamma]


def mean3(a, b, c):
    if a >= b and a >= c:
        if b >= c:
            return [0, 1, 2]
        else:
            return [0, 2, 1]
    elif b >= a and b >= c:
        if a >= c:
            return [1, 0, 2]
        else:
            return [1, 2, 0]
    elif c >= a and c >= b:
        if a >= b:
            return [2, 0, 1]
        else:
            return [2, 1, 0]
        
        
def genetic(x):
    for i in range(len(x) // 2):
        cut = rnd(0, lenth)
        for l in range(cut):
            a = x[i * 2][l]
            x[i * 2][l] = x[i * 2 + 1][l]
            x[i * 2 + 1][l] = a
            
            
def winner(x):
    max1 = -100
    k = -1
    for i in range(len(x)):
        if func(x[i]) > max1:
            k = i
            max1 = func(x[i])
    return x[k]
    



global lenth
lenth = 10
print(aproximation())