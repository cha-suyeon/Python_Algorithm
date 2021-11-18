# Section3

# 4. 데이터 삽입 함수의 완성

katok = ["다현", "정연", "쯔위", "사나", "지효"]

def insert_data(position, friend):
    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    katok.append(None)
    klen = len(katok)

    for i in range(klen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    
    katok[position] = friend

insert_data(2, '솔라')
print(katok)
insert_data(6, '문별')
print(katok)
insert_data(9, '화사')
print(katok)