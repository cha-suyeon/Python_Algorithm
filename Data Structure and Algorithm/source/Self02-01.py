## 함수 선언 부분 ##
def multi(v1, v2) :
    retList = []
    retList.append(v1 + v2)
    retList.append(v1 - v2)
    retList.append(v1 * v2)
    retList.append(v1 // v2)
    retList.append(v1 % v2)
    retList.append(v1 ** v2)
    return retList

## 전역 변수 선언 부분 ##
myList = []
hap, sub = 0, 0

## 메인 코드 부분 ##
myList = multi(100, 20)
print("multi()에서 반환한 값 ==> ", (myList))
