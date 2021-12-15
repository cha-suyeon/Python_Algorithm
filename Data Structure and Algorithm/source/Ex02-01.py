import random

## 전역 변수 선언 부분 ##
totalLotto = []
lotto = []
pickNum = 0
count = 0

## 메인 코드 부분 ##
print("** 로또 번호 생성을 시작합니다. **")
count = int(input('몇 번을 뽑을까요?'))

for _ in range(count) :
	 lotto = []
	 while True :
		  pickNum = random.randint(1, 45)
		  if pickNum not in lotto :
			   lotto.append(pickNum)
		  if len(lotto) >= 6 :
			   break
	 totalLotto.append(lotto)

for lotto in totalLotto :
	 lotto.sort()
	 print('자동번호--> ', end = ' ')
	 for i in range(0, 6) :
		  print("%2d" % lotto[i], end = ' ')
	 print()
