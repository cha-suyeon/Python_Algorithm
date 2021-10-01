# Section 2

katok = ["다현", "정연", "쯔위", "사나", "지효"]
print(katok)
print(katok[0])
print(katok[4])

# <데이터 삽입>
# 1. 선형 리스트에 빈칸 추가
katok.append(None)
print(katok)

# 2. 선형 리스트의 끝에 데이터 삽입
katok[5] = "모모"
print(katok)

# 3. 선형 리스트에 중간 데이터 삽입
katok.append(None)
print(katok)

# 3~5번째 데이터를 한 칸씩 옮기고 3번째 자리를 빈칸으로 만든다
katok[6] = katok[5]
katok[5] = None
print(katok)

katok[5] = katok[4]
katok[4] = None
katok[4] = katok[3]
katok[3] = None
print(katok)

katok[3] = "미나"
print(katok)

# <데이터 삭제> - "사나" 데이터 삭제

# 1. 4등 자리에 있던 데이터를 삭제한다.
katok[4] = None
print(katok)

# 2. 5등 자리에 있던 데이터를 4등 자리로 옮긴다.
katok[4] = katok[5]
katok[5] = None

# 3. 6등 자리에 있던 데이터를 5등 자리로 옮긴다.
katok[5] = katok[6]
katok[6] = None
print(katok)

# 4. 빈 6등 자리를 삭제한다.
del(katok[6])
print(katok)