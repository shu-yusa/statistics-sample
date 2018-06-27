# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import math
import random

def generate():
    r = random.random()
    return r
  
def variance(data):
    mu = 0
    x2 = 0
    for d in data:
        mu += d
        x2 += d * d
    mu /= len(data)
    x2 /= len(data)
    s2 = x2 - mu * mu
    return [s2 * len(data) / (len(data) - 1), s2]


if __name__=='__main__':
    data = []
    print(1/12)
    for j in range(0, 6):
        a = []
        for i in range(0, 10):
            a.append(generate())
        v = variance(a)
        print(str(v[0]) + ' : ' + str(v[1]))
    
