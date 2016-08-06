# чем меньше test, тем больше вероятность того, что p1 != p2

import math
import random
from matplotlib import pyplot as plt

M1 = int(input("Введите размер первой выборки: "))
N1 = int(input("Введите число успехов первой выборки: "))
M2 = int(input("Введите размер второй выборки: "))
N2 = int(input("Введите число успехов второй выборки: "))
size = int(input("Введите размер генерируемой выборки: "))

def h(x): # энтропия
    if x <= 0.0 or x >= 1.0:
        return 0.0
    else:
        return -x * math.log(x) - (1 - x) * math.log(1 - x)

def T(M1, N1, M2, N2): # целевая статистика, по которой проводится оценка
    return M1 * h(N1 / M1) + M2 * h(N2 / M2) - (M1 + M2) * h((N1 + N2) / (M1 + M2))

p_est = N1 / M1
Tlist = []
for i in range(size):
    A1 = 0
    A2 = 0
    for j in range(M1):
        if random.random() < p_est:
            A1 += 1
    for j in range(M2):
        if random.random() < p_est:
            A2 += 1
    Tlist.append(T(M1, A1, M2, A2))
Tlist.sort()
Ylist = [(i + 1) / size for i in range(size)]
plt.plot(Tlist, Ylist, label = 'CDF')
plt.plot([T(M1, N1, M2, N2) for i in Tlist], Ylist, label = 'test')
plt.grid()
plt.legend(loc = 'best')
plt.show()
plt.close()
