import math



def main(z, x, y):
    n = len(x)
    sum = 0
    for i in range(1, n + 1):
        sum += 82 * (44 * (y[math.ceil((i / 4) - 1)] ** 2) - x[n - i] - 7 * (z[math.ceil((i / 4)-1)] **3))**6
    return sum


print(main([-0.85, 0.17, -0.51, 0.97], [-0.37, 0.8, 0.31, 0.26], [-0.84, -0.81, -0.4, -0.45]))
