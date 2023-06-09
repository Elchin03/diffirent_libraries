import math



def main(z, x, y):
    n = len(x)
    sum = 0
    for i in range(1, n + 1):
        sum += 82 * (44 * (y[math.ceil((i / 4) - 1)] ** 2) - x[n - i] - 7 * (z[math.ceil((i / 4)-1)] **3))**6
    return sum


print(main([-0.72, -0.8, 0.5, 0.35],
[0.48, 0.9, -0.56, 0.37],
[0.77, -0.69, -0.5, 0.75]))
