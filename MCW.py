import numpy as np
import math as mt
import matplotlib.pyplot as plt


def Model (n):
    S0=np.zeros((n))
    for i in range(n):
        S0[i]=(0.0000005*i*i)
    return S0

def NORM (dm, dsig, iter):
    S = np.random.normal(dm, dsig, iter)
    mS = np.median(S)
    dS = np.var(S)
    scvS = mt.sqrt(dS)
    return S

def Model_NORM (SN, S0N, n):
    SV=np.zeros((n))
    for i in range(n):
        SV[i] = S0N[i]+SN[i]
    return SV
n = 5000
iter = int(n)
dm = 0
dsig = 10
S0 = Model(n)
S = NORM(dm, dsig, iter)
SV = Model_NORM(S, S0, n)

mS = np.median(SV)
dS = np.var(SV)
scvS = mt.sqrt(dS)
print('------- статистичні характеристики Н-----')
print('матиматичне сподівання ВВ=', mS)
print('дисперсія ВВ =', dS)
print('СКВ ВВ=', scvS)
print('------------------------------------------------------------------')
def Plot_AV (S0_L, SV_L, Text):
    plt.plot(SV_L)
    plt.plot(S0_L)
    plt.ylabel(Text)
    plt.show()
    return
Plot_AV(S0, SV, 'квадратична модель + Норм.Похибка')