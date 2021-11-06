from random import randrange as rnd, choice
import numpy as np


def aproximation():
    n = 30
    pops = []
    for i in range(n):
        pops.append([rnd(0, 2) for i in range(lenth)])    
    pops_clone = pops.copy()
    ''' separation of individuums '''
    for i in range(10000):
        alpha = turnir(pops)[0]
        betta = turnir(pops)[1]
        for l in range(2 * n // 3, n):
            pops[l] = pops[l - 2 * n // 3].copy()        
        genetic(alpha)
        genetic(betta)
        for l in range(n // 3):
            pops[l] = alpha[l].copy()
        for l in range(n // 3, 2 * n // 3):
            pops[l] = betta[l - n // 3].copy() 
        for i in range(n // 5):
            mutation(pops[rnd(0, n)])
    return winner(pops)
            
    

    
def func(x):
    s = 0
    w = 0
    for i in range(lenth):
        s += x[i] * things[i][0]
        w += x[i] * things[i][1]
    if w > weight:
        s = 0
    return [s, w]


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
        m_a = func(a)[0]
        m_b = func(b)[0]
        m_c = func(c)[0]
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
        for l in range(lenth // 2):
            element = rnd(0, lenth)
            a = x[i * 2][element]
            x[i * 2][element] = x[i * 2 + 1][element]
            x[i * 2 + 1][element] = a
            
            
def mutation(x):
    a = rnd(0, lenth)
    x[a] = (x[a] + 1) % 2
    pass
            
            
def winner(x):
    max1 = -100
    k = -1
    for i in range(len(x)):
        if func(x[i])[0] > max1 and func(x[i])[1] <= weight:
            k = i
            max1 = func(x[i])[0]
    if k == -1:
        return 'None'
    else:
        return x[k], func(x[k])


def massiv_generation():
    global things
    things = [[5, 6], [3, 4], [1, 3], [3, 2], [6 , 5]]
    
    
'''def analitic(w, k):
    a = [[0] * (w + 1) for i in range(k + 2)]
    for i in range(1, k + 1, 1):
        for l in range(w + 1):
            a[i][l] = a[i - 1][l]
            if l >= things[i][1] and a[i - 1][l - things[i][1]] + things[i][0] > a[i][l]:
                a[i][l] = a[i - 1][l - things[i][1]] + things[i][0]
    print(a)
'''

global lenth, things, weight
weight = 15
massiv_generation()
lenth = len(things)
print(aproximation())