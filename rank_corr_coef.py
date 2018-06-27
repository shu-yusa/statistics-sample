# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import math

def spearman(x, y):
    r = 0
    n = len(x)
    for i in range(0, n):
        r += (x[i] - y[i]) * (x[i] - y[i])

    r = 1 - 6 / (n ** 3  - n) * r
    return r

def kendall(x, y):
    G = 0
    H = 0
    n = len(x)
    for i in range(0, n):
        for j in range(i+1, n):
            if (x[i] > x[j] and y[i] > y[j]) or (x[i] < x[j] and y[i] < y[j]):
                G += 1
            else:
                H += 1

    r = (G - H) / n / (n - 1) * 2
    return r


if __name__=='__main__':

    x = range(1, 31)
    y = [1, 5, 2, 3, 6, 7, 15, 8, 4, 11,
            10, 14, 18, 13, 22, 24, 16, 19, 30, 9,
            25, 17, 26, 23, 12, 20, 28, 21, 27, 29]
    z = [8, 3, 1, 4, 2, 5, 11, 7, 15, 9,
            6, 13, 10, 22, 12, 14, 18, 19, 17, 22,
            16, 24, 21, 20, 28, 30, 25, 26, 27, 29]
    w = [20, 1, 4, 2, 6, 3, 12, 17, 8, 5,
            18, 13, 23, 26, 29, 15, 16, 9, 10, 11,
            30, 7, 27, 19, 14, 21, 28, 24, 22, 25]

    print('x and y')
    print(spearman(x, y))
    print(kendall(x, y))
    print('x and z')
    print(spearman(x, z))
    print(kendall(x, z))
    print('x and w')
    print(spearman(x, w))
    print(kendall(x, w))
    print('y and z')
    print(spearman(y, z))
    print(kendall(y, z))
    print('y and w')
    print(spearman(y, w))
    print(kendall(y, w))
    print('y and z')
    print(spearman(y, z))
    print(kendall(y, z))
    print('w and z')
    print(spearman(w, z))
    print(kendall(w, z))
