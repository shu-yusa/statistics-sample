# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import math
import random
import scipy.stats as stats

def calc_two_sample_t_stat(x, y):
    """
    2標本から、標本平均が等しいという仮説下でのt統計量を計算する
    @param データ1
    @param データ2
    @return t統計量
    """
    # numPyのライブラリを使用して平均、不偏分散を計算
    meanX, s2x = np.mean(x), np.var(x, ddof=1)
    meanY, s2y = np.mean(y), np.var(y, ddof=1)
    n_x = len(x)
    n_y = len(y)

    # 合併した分散
    s2 = ((n_x - 1) * s2x + (n_y - 1) * s2y) / (n_x + n_y - 2)
    # t統計量
    t = (meanX - meanY) / math.sqrt((1 / n_x + 1 / n_y) * s2)

    return [n_x + n_y - 2, t]

def welch_t_stat(x, y):
    meanX, s2x = np.mean(x), np.var(x, ddof=1)
    meanY, s2y = np.mean(y), np.var(y, ddof=1)
    n_x = len(x)
    n_y = len(y)

    # 自由度
    nu = (s2x / n_x + s2y / n_y)**2 / ((s2x / n_x)**2 / (n_x - 1) + (s2y / n_y)**2 / (n_y - 1))

    # t統計量
    t = (meanX - meanY) / math.sqrt(s2x / n_x + s2y / n_y)

    return [nu, t]

def f_stat(x, y):
    return np.var(x, ddof=1) / np.var(y, ddof=1)

if __name__=='__main__':
    # 男性賃金
    x = [15.4, 18.3, 16.5, 17.4, 18.9, 17.2, 15.0, 15.7, 17.9, 16.5]
    # 女性賃金
    y = [14.2, 15.9, 16.0, 14.0, 17.0, 13.8, 15.2, 14.5, 15.0, 14.4]
    n_x = len(x)
    n_y = len(y)

    # ----------------- 等母分散仮定でのt検定 ---------------------
    print("-------- t検定 ----------")
    # 2標本から計算したt統計量
    dof, t = calc_two_sample_t_stat(x, y)
    # 自由度(n_x + n_y - 2)のt分布の上側2.5パーセント点
    t_975 = stats.t.ppf(0.975, dof)
    print("t値:", t) 
    print("上側2.5%点:", t_975)
    if (t > t_975):
        print("仮説を棄却")
    else:
        print("仮説は棄却されない")

    # Scipyによる2標本等平均のt検定
    print()
    print("--- t検定(scipyを使用) ---")
    t, p = stats.ttest_ind(x, y)
    print("t値:", t) 
    print("p値:", p)
    if (p < 0.025):
        print("仮説を棄却")
    else:
        print("仮説は棄却されない")


    # --------------------- Welchの検定 ------------------------
    print()
    print("--- Welchの検定 ---")
    # Welchの検定
    dof, t = welch_t_stat(x, y)
    print("自由度:", dof, "=>", round(dof))
    print("t値:", t)
    dof = round(dof)
    # t分布の上側2.5パーセント点
    t_975 = stats.t.ppf(0.975, dof)
    print("上側2.5%点:", t_975)
    if (t > t_975):
        print("仮説を棄却")
    else:
        print("仮説は棄却されない")

    print("--- Welchの検定(scipy) ---")
    # Scipyによる2標本等平均のt検定
    t, p = stats.ttest_ind(x, y, equal_var=False)
    print("t値:", t) 
    print("p値:", p)
    if (p < 0.025):
        print("仮説を棄却")
    else:
        print("仮説は棄却されない")


    # ---------------------- 母分散比のF検定 ---------------------
    print()
    print("--- 母分散比のF検定 ---")
    f = f_stat(x, y)
    print("F値:", f)
    # 下側0.5パーセント点
    fu = stats.f.ppf(0.995, n_x - 1, n_y - 1)
    # 上側0.5パーセント点
    fl = stats.f.ppf(0.005, n_x - 1, n_y - 1)
    print("下側0.5%点:", fl)
    print("上側0.5%点:", fu)
    if (f > fu or f < fl):
        print("仮説を棄却")
    else:
        print("仮説は棄却されない")


