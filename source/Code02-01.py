## 함수 선언 부분 ## 
def plus( v1, v2) :
	result = 0
	result = v1 + v2
	return result

## 전역 변수 부분 ## 
hap = 0

## 메인 코드 부분 ## 
hap = plus(100, 200)
print("100과 200의 plus() 함수 결과는 %d" % hap)
