from matplotlib import pyplot as plt
import numpy as np
import re
import sys
import math

# prepare...
regexp = re.compile(r'([0-9\.]+)\s([0-9\.]+)')
x = []
y = []

# read data arrays
size = int(input('Input data size: '))
print('Input data')
for i in range(size):
    data = input()
    if regexp.match(data):
        x.append(float(regexp.search(data).group(1)))
        y.append(float(regexp.search(data).group(2)))
    else:
        print('Invalid input!')
        sys.exit()

# calculate mean and variation
mean = 0
for i in range(size):
    mean += x[i] * y[i]
mean /= sum(y)
var = 0
for i in range(size):
    var += (x[i] - mean) ** 2 * y[i]
var /= sum(y)

# calculate data for gaussian
delta = max(x) - min(x)
fx = [(min(x) - delta / 10) + i * delta * 1.2 / 100 for i in range(101)]
fy = [sum(y) * math.exp( - (x - mean) ** 2 / 2 / var) / math.sqrt(2 * math.pi * var) for x in fx]

#plot graph
plt.plot(fx, fy, 'g', label = 'Gauss')
plt.stem(x, y, label = 'Sample')
plt.grid()
plt.legend()
plt.show()
plt.close()
