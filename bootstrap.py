# coding:utf-8
# ブートストラップ法により相関係数の分布を作成する

import numpy as np
import matplotlib.pyplot as plt
import math
import random

def corr_coef(x, y):
    u"""
    相関係数を計算する関数
    @param x データ1
    @param y データ2
    @return 相関係数
    """

    # 初期化
    Sx = Sy = 0
    meanX = meanY = 0

    # 一つ目のデータ
    for a in x:
        meanX += a
        Sx += a * a
    # 標本のサイズ
    size = len(x)
    # 標本平均
    meanX /= size
    # 標準偏差
    Sx = math.sqrt(Sx / size - meanX * meanX)

    # 二つ目のデータ
    for a in y:
        meanY += a
        Sy += a * a
    # 標本のサイズ
    size = len(y)
    # 標本平均
    meanY /= size
    # 標準偏差
    Sy = math.sqrt(Sy / size - meanY * meanY)

    # 相関係数の計算
    r = 0;
    for i in range(0, size):
        r += (x[i] - meanX) * (y[i] - meanY)

    r = r / size / Sx / Sy

    return r


if __name__=='__main__':
    # 一つ目の標本データ
    x = [71, 68, 66, 67, 70, 71, 70, 73, 72, 65, 66]
    # 二つ目の標本データ
    y = [69, 64, 65, 63, 65, 62, 65, 64, 66, 59, 62]

    # ヒストグラム用の配列
    r_a = []
    
    # ブートストラッピング
    for i in range(2000):
        a = []
        b = []
        # 標本再抽出(復元抽出)
        for j in range(10):
            r = random.randint(0, 10)
            a.append(x[r])
            b.append(y[r])

        # 配列に格納
        r_a.append(corr_coef(a, b))

    # print(r_a)

    # ヒストグラムにして表示
    plt.hist(r_a, bins=20)
    plt.show()


