# Section3

# 2. 선형 리스트 생성 함수의 완성
# 선형 리스트의 끝에 데이터를 추가하는 함수 작성하여 5명을 차례대로 추가하는 완전한 코드

katok = []

def add_data(friend):

    katok.append(None)
    klen = len(katok)
    katok[klen-1] = friend

add_data("다현")
add_data("정연")
add_data("쯔위")
add_data("사나")
add_data("지효")

print(katok)