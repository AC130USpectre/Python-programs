import numpy
import matplotlib.pyplot as plt

str = input('DataPath: ')
x = numpy.genfromtxt(str).tolist()
y = [i / len(x) for i in range(0, len(x))]
x.sort()
a = (max(x)-min(x)) / 10
x = [x[0] - a] + x + [x[-1]+a]
y = [0] + y + [1]
plt.step(x, y, label = 'EDF')
plt.axis([x[0] + a / 2, x[-1] - a / 2, 0.0, 1.05])
plt.legend(loc = 2)
plt.xlabel('$x$')
plt.ylabel('${\cal P}(data < x)$')
plt.title('Empirical Distribution Function')
plt.grid()
plt.savefig('edf.png')
plt.show()
plt.close()
