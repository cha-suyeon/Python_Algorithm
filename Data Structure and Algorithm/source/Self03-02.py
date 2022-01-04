## 함수 선언부
def printPoly(p_x) :
    term = len(p_x) - 1 # 최고항 숫자 = 배열길이 -1
    polyStr = "P(x) = "
    
    for i in range(len(px)) :
        coef = p_x[i] # 계수

        if coef == 0 : # 계수가 0이면 생략
            term -= 1
            continue
        if (coef >= 0 and i != 0) : # 제일 앞의 +는 출력 안되도록
           polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "
        term -= 1

    return polyStr

def calcPoly(xVal, p_x) :
    retValue = 0
    term = len(p_x) - 1 # 최고항 숫자 = 배열길이 -1
    
    for i in range(len(px)) :
        coef = p_x[i] # 계수
        retValue += coef * xValue ** term
        term -= 1

    return retValue


## 전역 변수 선언부
px = [7, -4, 0, 5] # = 7x^3  -4x^2  + 0x^1 +  5x^0 

## 메인 코드
if __name__ == "__main__" :

    pStr = printPoly(px)
    print(pStr)

