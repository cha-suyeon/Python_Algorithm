# Section5

# 5. 데이터 삭제

katok = ["다현", "정연", "쯔위", "사나", "지효"]

# katok[position] = None
# for i in range(position+1, klen+1):
#   katok[i-1] = katok[i]
#   katok[i] = None
# del(katok[position])

# 데이터 삭제 함수의 완성
def delete_data(position):
    if position < 0 or position > len(katok):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    klen = len(katok)
    katok[position] = None

    for i in range(position+1, klen):
        katok[i-1] = katok[i]
        katok[i] = None
    
    del(katok[klen-1])

delete_data(1)
print(katok)
delete_data(3)
print(katok)
