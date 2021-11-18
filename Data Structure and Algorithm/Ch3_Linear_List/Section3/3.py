# Section3

# 3. 데이터 삽입
# 선형 리스트에 데이터를 삽입하는 방식을 구현
# 선형 리스트의 지정 위치에 데이터를 삽입하는 과정을 2번 인덱스에 삽입

# 1) 데이터 초기 상태
katok = ["다현", "정연", "쯔위", "사나", "지효"]

# 2) 선형 리스트에 빈칸 추가
katok.append(None)

# 3) 자리 이동
klen = len(katok)
for i in range(klen-1, position, -1):
    katok[i] = katok[i-1]
    katok[i-1] = None

katok[position] = friend

# 이를 바탕으로 데이터 삽입 함수를 구현한다.