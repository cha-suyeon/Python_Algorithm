## 함수 선언 부분 ##
def find_and_insert_data(friend, k_count) :
	findPos = -1
	for i in range(len(katok)) :
		pair = katok[i]
		if k_count >= pair[1] :
			findPos = i
			break
	if findPos == -1 :
		findPos = len(katok)

	insert_data(findPos, (friend, k_count))


def insert_data(position, friend):
	if position < 0 or position > len(katok):
		print("데이터를 삽입할 범위를 벗어났습니다.")
		return

	katok.append(None)	# 빈 칸 추가
	kLen = len(katok)		# 배열의 현재 크기

	for i in range(kLen - 1, position, -1):
		katok[i] = katok[i - 1]
		katok[i - 1] = None

	katok[position] = friend


## 전역 변수 선언 부분 ##
katok = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]

## 메인 코드 부분 ##
if __name__ == "__main__":

	while True:
		data = input("추가할 친구--> ")
		count = int(input("카톡 횟수--> "))
		find_and_insert_data(data, count)
		print(katok)
