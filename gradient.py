from random import randint
# y = t0 * x + t1


def func(t: list, x: list, y: list):
    summ = 0
    for i in range(len(x)):
        summ += (y[i] - (t[0] * x[i] - t[1])) ** 2
    return summ / len(x)


def grad_func(t, x, y):
    summ1, summ2 = 0, 0
    for i in range(len(x)):
        summ1 += (y[i] - (t[0] * x[i] - t[1])) * (-x[i])
        summ2 += y[i] - (t[0] * x[i] - t[1])
    grad1 = 2 * summ1 / len(x)
    grad2 = 2 * summ2 / len(x)
    return grad1, grad2


def GD_classic(t, x, y):    
    for i in range(50000):
        d0, d1 = grad_func(t, x, y)
        t[0] = t[0] - d0 * 0.01
        t[1] = t[1] - d1 * 0.01
        #print(t)
        #print(func(t, x, y))
        
        
def SGD(t, x, y):
    for i in range(50000):
        x0 = randint(0, len(x) - 1)
        d0, d1 = grad_func(t, [x[x0]], [y[x0]])
        t[0] -= 0.01 * d0
        t[1] -= 0.01 * d1
        #print(func(t, [x[x0]], [y[x0]]))
        
        
def Mini_Batch(t, x, y):
    for i in range(50000):
        x1 = randint(0, len(x) - 1)
        x2 = randint(0, len(x) - 1)
        d0, d1 = grad_func(t, [x[x1], x[x2]], [y[x1], y[x2]])
        t[0] -= 0.01 * d0
        t[1] -= 0.01 * d1
        #print(func(t, [x[x0]], [y[x0]]))
    
    
t = [1, 1]
x = [1, 2, 3]
y = [2, 4, 100]
GD_classic(t, x, y)
print('GD classic:', func(t, x, y))

t = [1, 1]
x = [5, 6, 7]
y = [3, 4, 5]
SGD(t, x, y)
print('SGD:', func(t, x, y))

t = [1, 1]
x = [5, 6, 7]
y = [3, 4, 5]
Mini_Batch(t, x, y)
print('Mini_Batch:', func(t, x, y))