def main(n):
    return{
        "T1": (n & 0b1111111),
        "T2": ((n >> 7 ) & 0b111),
        "T4": ((n >> 18) & 0b1111111111111)

    }#целое декодирование
print(main(11469761))