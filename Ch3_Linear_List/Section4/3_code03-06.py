# Section4

# 3. 특수 다항식 처리 프로그램
# 만약 지수가 상당히 큰 다항식은 어떻게 처리할 것인가?

# px = [7, 0, 0, 0, 0, ..., -4, 0, 0, 0, ..., 5] - 총 301개

# 이는 현실적으로 처리하기 어렵다.
# 이를 간단히 처리하고자 모든 계수를 저장하지 않고 0이 아닌 계수와 항의 차수만 저장하는 방식 사용

# tx = [300, 20, 0]  # 항 차수
# px = [7, -4, 5]    # 각 항 위치의 계수

## 함수 선언 부분 ## 
def printpoly(t_x, p_x):
    polystr = "P(x)= "

    for i in range(len(p_x)):
        term = t_x[i]           # 항 차수
        coef = p_x[i]           # 계수

        if (coef >= 0):
            polystr += "+"
        polystr += str(coef) + 'x^' + str(term) + ' '

    return polystr

def calcpoly(xval, t_x, p_x):
    retvalue = 0

    for i in range(len(px)):
        term = t_x[i]           # 항 차수
        coef = p_x[i]           # 계수
        retvalue += coef + xvalue ** term
        term -= 1

    return retvalue

## 전역 변수 선언 부분 ##
tx = [300, 20, 0]               # 항 차수
px = [7, -4, 5]                 # 각 항 위치의 계수

## 메인 코드 부분 ##
if __name__ == "__main__":

    pstr = printpoly(tx, px)
    print(pstr)

    xvalue = int(input('X 값--> '))
    
    pxvalue = calcpoly(xvalue, tx, px)
    print(pxvalue)

