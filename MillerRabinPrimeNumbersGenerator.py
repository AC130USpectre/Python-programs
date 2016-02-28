#generate prime number
#use miller-rabin test to check that number is prime

import math
import random
import time
import ModuleOperators

def mr_num(n):
    (r, s) = (n - 1, 0)
    while r % 2 == 0:
        r //= 2
        s += 1
    return (r, s)

def isPrime(number, rounds):
    #checking by list of prime numbers
    f = open('prime_numbers_list.txt', 'r')
    for line in f:
        if number % int(line) == 0:
            return False
    f.close()
    #miller-rabin test
    (r, s) = mr_num(number)
    seed = time.time()
    for i in range(rounds):
        is_prob_prime = False
        seed += i
        random.seed(seed)
        a = random.randint(2, number - 2)
        a = ModuleOperators.power(a, r, number)
        if a == 1 or a == (number - 1):
            continue
        for j in range(s):
            a = ModuleOperators.power2(a, number)
            if a == (number - 1):
                is_prob_prime = True
                break
        if not is_prob_prime:
            return False
    return True

def generatePrime(length, rounds):
    while True:
        random.seed()
        candidate = random.randint(2 ** length, 2 ** (length + 1))
        if (isPrime(candidate, rounds)):
            return candidate

file = open('primeNumber_P.txt', 'w')
file.write(str(generatePrime(512, 2048)))
file.close()

time.sleep(10)

file = open('primeNumber_Q.txt', 'w')
file.write(str(generatePrime(512, 2048)))
file.close()
