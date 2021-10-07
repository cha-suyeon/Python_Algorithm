## 함수 선언 부분 ## 
def printpoly(p_x):
    polystr = "P(x)= "

    for i in range(len(p_x[0])):
        term = p_x[0][i]           # 항 차수
        coef = p_x[1][i]           # 계수

        if (coef >= 0):
            polystr += "+"
        polystr += str(coef) + 'x^' + str(term) + ' '

    return polystr


def calcpoly(xval, p_x):
    retvalue = 0

    for i in range(len(p_x[0])):
        term = p_x[0][i]           # 항 차수
        coef = p_x[1][i]           # 계수
        retvalue += coef + xvalue ** term
        term -= 1

    return retvalue


## 전역 변수 선언 부분 ##
px = [[300,20,0],
    [7,-4,5]]


## 메인 코드 부분 ##
if __name__ == "__main__":

    pstr = printpoly(px)
    print(pstr)

    xvalue = int(input('X 값--> '))
    
    pxvalue = calcpoly(xvalue, px)
    print(pxvalue)