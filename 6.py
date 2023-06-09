def main(x: list):
    if x[0] == 1988:
        if x[2] == 2009:
            if x[1] == 'VUE':
                return 0
            if x[1] == 'HYPHY':
                if x[4] == 1962:
                    return 1
                if x[4] == 1981:
                    return 2
        if x[2] == 2007:
            return 3
        if x[2] == 1999:
            if x[4] == 1962:
                if x[1] == 'VUE':
                    return 4
                if x[1]=="HYPHY":
                    return 5
            if x[4] == 1981:
                if x[3] == "CIRRU":
                    return 6
                if x[3] == "EAGLE":
                    return 7
                if x[3] == "SASS":
                    return 8
    if x[0] == 1970:
        if x[2] == 2009:
            return 9
        if x[2] == 2007:
            return 10
        if x[2]== 1999:
            return 11
    if x[0]== 1996:
        return  12
print(main([1996, 'VUE', 1999, 'EAGLE', 1962]))