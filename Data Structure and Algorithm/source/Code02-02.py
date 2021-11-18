## 함수 선언 부분 ## 
def func1():
	a = 10  # 지역 변수
	print("func1()에서 a 값 %d" % a)

def func2():
	print("func2()에서 a 값 %d" % a)

## 전역 변수 부분 ## 
a = 20  # 전역 변수

## 메인 코드 부분 ## 
func1()
func2()
