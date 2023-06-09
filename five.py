import math
from math import tan


def five(z, x):
    n = len(x)
    sum = 0
    for i in range(1, n + 1):
        sum += 72 * (tan(2 * (x[i - 1]) ** 2 - 74 - 28 * (z[n - math.ceil(i / 2)] **3)) ** 4)
    return 46 * sum
print(five([-0.99, 0.24, -0.62],
[-0.9, 0.87, -0.75]))
