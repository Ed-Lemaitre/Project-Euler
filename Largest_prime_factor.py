#What is the largest prime factor of the number 600851475143 ?

from eulermodule import get_primes
from math import sqrt

N = 600851475143
lista = list(reversed(get_primes(int(sqrt(N)+1))))

for i in lista:
    if not N%i:
        print(i)
        break