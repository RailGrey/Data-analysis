import random
#import numpy as np
import math
import pandas as pd



def fire(x, y, t):
    iterat = 1000000
    f = func(x, y)
    min1 = 10000000
    a = 0.5
    #t = 10
    dt = t / iterat
    for i in range(iterat):
        x1 = random.uniform(x - a * t ** 2, x + a * t ** 2)
        y1 = random.uniform(y - a * t ** 2, y + a * t ** 2)
        f1 = func(x1, y1)
        if f1 < min1:
            min1 = f1
        if (f - f1) / t >= 1:
            ver = 1
        else:
            ver = math.exp((f - f1) / t)
        if ver >= 1:
            check = True
        else:
            check = random.choices([True, False], weights = [ver, 1 - ver])
        if check:
            x = x1
            y = y1
            f = f1
            t = t - dt
    return min1

def func(x, y):
    #return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2
    #a = -20 * math.exp(-0.2 * (0.5 * (x ** 2 + y ** 2) ** 0.5)) - math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) + math.e + 20 
    #return a
    return x ** 2 + y ** 2

'''
n = 5
local_min = [0 for i in range(n)]
x_0 = [0 for i in range(n)]
y_0 = [0 for i in range(n)]
for i in range(n):
    x_0[i] = random.uniform(-100, 100)
    y_0[i] = random.uniform(-100, 100)
    local_min[i] = fire(x_0[0], y_0[0], (i + 1) * 0.01)

df = pd.DataFrame()  
for i in range(n):
    new_store = [{'x' : x_0[i], 'y' : y_0[i], 'min' : local_min[i]}]
    df = df.append(new_store)
    #print('x =' + str(x_0[i]) + 'y =' + str(y_0[i]) + 'f_min = ' + str(local_min[i]))
print(df)
'''
print(fire(50, 50, 5))