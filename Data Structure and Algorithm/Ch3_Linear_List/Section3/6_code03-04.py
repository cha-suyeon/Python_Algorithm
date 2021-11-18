# Section3

# 6. 기본 선형 리스트의 완성
# code03-01~code03-03까지 작성한 함수 3개를 통합해서 완전한 선형 리스트를 처리하는 프로그램을 완성하자.
# 이 프로그램은 처음에는 빈 선형 리스트에서 데이터 입력, 중간 삽입, 삭제를 사용자가 원하는 만큼 반복할 수 있다.

## 함수 선언 부분 ##
def add_data(frined):
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = frined

def insert_data(position, friend):
    if position < 0 or position > len(katok):
        # '<' not supported between instances of 'str' and 'int'
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    katok.append(None)
    klen = len(katok)

    for i in range(klen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    
    katok[position] = friend

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

## 전역 변수 선언 부분 ##
katok = []
select = -1 # 1: 추가, 2: 삽입, 3: 삭제, 4: 종료

## 메인코드 부분 ##
if __name__=="__main__":

    while(select != 4):
        select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)-->"))
        if (select==1):
            data = input('추가할 데이터--> ')
            add_data(data)
            print(katok)
        elif (select==2):
            pos = int(input('삽입할 위치--> '))
            data = input('추가할 데이터--> ')
            insert_data(pos, data)
            print(katok)
        elif (select==3):
            pos = int(input('삭제할 위치--> '))
            delete_data(pos)
            print(katok)
        elif (select==4):
            print(katok)
            exit
        else:
            print('1~4 중 하나를 입력하세요.')
            continue
