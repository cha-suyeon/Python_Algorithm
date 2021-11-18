# Section4

# 다항식의 선형 리스트 표현
px = [7, -4, 0, 5]

x = 2
pxval = 7*x**3 - 4*x**2 + 0*x**1 + 5*x**0
print(pxval)

polystr = "P(X)="
polystr += "+" + str(px[0]) + "x^" + str(3)
polystr += "+" + str(px[1]) + "x^" + str(2)
polystr += "+" + str(px[2]) + "x^" + str(1)
polystr += "+" + str(px[3]) + "x^" + str(0)
print(polystr)