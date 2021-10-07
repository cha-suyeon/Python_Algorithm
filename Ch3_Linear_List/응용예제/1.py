## 함수 선언 부분 ##
def find_and_insert_data(friend, k_count):
    findPos = -1                                # 새 친구 위치 -1 로 설정
    for i in range(len(katok)):                 # katok 친구 수만큼 반복
        pair = katok[i]                         # 현재 친구의 연락 횟수 추출
        if k_count >= pair[1]:                  # 새 친구의 연락 횟수와 비교
            findPos = i                         # 새 친구 연락 횟수가 더 크면 현재 위치로 설정
            break
    if findPos == -1:                           # 새 친구 위치가 계속 -1이라면 위치를 못 찾은 것
        findPos = len(katok)                    # 맨 뒤로 위치를 설정해준다.
    
    insert_data(findPos, (friend, k_count))     # 새 친구의 위치를 찾았고, (친구 이름, 연락 횟수)를 삽입한다.


def insert_data(position, friend):              # 새 친구 삽입 코드
    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    katok.append(None)      # 빈칸 추가
    kLen = len(katok)       # 배열의 현재 크기

    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    
    katok[position] = friend


## 전역 변수 선언 부분 ##
katok = [('다현', 200), ('정연', 130), ('쯔위', 90), ('사나', 30), ('지효', 15)]    # 초기 친구 목록

## 메인 코드 부분 ##
if __name__ == "__main__":

    while True:
        data = input("추가할 친구--> ")
        count = int(input("카톡 횟수--> "))
        find_and_insert_data(data, count)           # 새 친구 삽입
        print(katok)                                # 추가된 값 출력

# 새로운 친구 삽입을 그만하고 싶으면 'ctrl+c' 클릭