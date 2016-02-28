#some useful operations in module arithmetic

def power2(base, mod):
    return (base ** 2) % mod

def prod(num1, num2, mod):
    return (num1 * num2) % mod

def power(base, exp, mod):
    k = 0
    while exp >> k != 0:
        k += 1
    k -= 1
    result = base
    for i in range(k - 1, -1, -1):
        if 1 << i & exp == 0:
            result = power2(result, mod)
        else:
            result = prod(power2(result, mod), base, mod)
    return result

def euclid(a, b):
    if a % b == 0:
        return b
    else:
        return euclid(b, a % b)

def extEuclid(a, b):
    R_last = a
    R_now = b
    R_fut = R_last % R_now
    Q_last = 1
    Q_now = 0
    P_last = 0
    P_now = 1
    while R_fut > 0:
        G = R_last // R_now
        R_fut = R_last % R_now
        P_fut = P_last - P_now * G
        Q_fut = Q_last - Q_now * G
        R_last = R_now
        R_now = R_fut
        P_last = P_now
        P_now = P_fut
        Q_last = Q_now
        Q_now = Q_fut
    return (Q_last, P_last, a * Q_last + b * P_last)
