def main(x:str):
 i = int(x)
 y1 = 0b1111 & i
 y2 = 0b1 & (i >> 4)
 y3 = 0b1111 & (i >> 5)
 y4 = 0b111111111 & (i >> 9)
 y5 = 0b111111111 & (i >> 18)
 y6 = 0b11111111111 & (i >> 27)
 i1= hex(y1)
 i2= hex(y2)
 i3= hex(y3)
 i4= hex(y4)
 i5= hex(y5)
 i6= hex(y6)
 return tuple(map(str,(i1,i2,i3,i4,i5,i6)))

print(main(18162738047))
