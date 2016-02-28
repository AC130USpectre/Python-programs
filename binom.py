import math
import numpy
import matplotlib.pyplot as plt

def C(k, n):
    return math.exp(math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1))
def P(k, n, p):
    return C(k, n) * math.pow(p, k) * math.pow(1 - p, n - k)

n = int(input("n = "))
p = float(input("p = "))
xlist = numpy.arange(0, n+1, 1)
ylist = [P(x, n, p) for x in xlist]
plt.stem(xlist, ylist, markerfmt='ro', basefmt='--')
plt.grid()
plt.axis([-0.5, n + 0.5, 0.0, max(ylist)*1.05])
plt.xlabel('$k$')
plt.ylabel('$C^k_n p^k (1-p)^{n-k}$')
plt.title('$n = ' + str(n) + ', p = ' + str(p) + '$')
plt.savefig('binom.png')
plt.show()
plt.close()
