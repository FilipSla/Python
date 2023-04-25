import random as random

"Loop"
n = random.randrange(1, 11)
[print(i**2) for i in range(n)]

"Print Function"
s = ""
for num in range(1, n + 1):
    s += str(num)
print(s)
print(*[str(num) for num in range(1, n + 1)], sep="")