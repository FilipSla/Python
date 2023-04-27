import random
import time


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(pow(number, 0.5)) + 1):
        if number % i == 0:
            return False
    return True


tic = time.perf_counter()
n = int(("1 000").replace(" ", ""))
collectionOfPrimeNumbers = list()
# For loop
# [collectionOfPrimeNumbers.append(i) for i in range(1, n + 1) if is_prime(i)]
test = (i for i in range(1,n+1) if is_prime(i)) #generátor

# While loop
"""
i = 0
while i < n + 1:
    if is_prime(i):
        collectionOfPrimeNumbers.append(i)
    i += 1
"""
toc = time.perf_counter()
print(f"Výpočet prvočísel do {n} trval {toc - tic:0.4f} sekund")
help(__doc__)
