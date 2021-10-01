# Section4

# 다항식 선형 리스트 표현과 계산 프로그램

## 함수 선언 부분 ##
def printpoly(p_x):
    term = len(p_x)-1 # 최고차항 숫자 = 배열 길이 - 1
    polystr = "P(x)= "

    for i in range(len(px)):
        coef = p_x[i] # 계수

        if (coef >= 0):
            polystr += "+"
        polystr += str(coef) + "x^" + str(term) + " "
        term -= 1

    return polystr

def calcpoly(xval, p_x):
    retvalue = 0
    term = len(p_x)-1 # 최고차항 숫자 = 배열 길이-1

    for i in range(len(px)):
        coef = p_x[i]
        retvalue += coef * xvalue ** term
        term -= 1

    return retvalue

## 전역 변수 선언 부분 ##
px = [7, -4, 0, 5]

## 메인 코드 부분 ##
if __name__ == "__main__":
    pstr = printpoly(px)
    print(pstr)

    xvalue = int(input("X 값--> "))

    pxvalue = calcpoly(xvalue, px)
    print(pxvalue)
