# 하샤드 수

## 나의 첫 번째 틀린 풀이
def solution(x):
    answer = True
    x = [int(i) for i in str(x)]
    sum_x = sum(x)
    
    if x % sum_x:
        answer = 'true'
    else:
        answer = 'false'
    
    return answer

# TypeError: unsupported operand type(s) for %: 'list' and 'int'
# x를 list로 변경 시켜주야 해서 list로 int를 나눗셈 연산을 못한다.
# 여기서 x를 다시 str -> int 해주는 과정을 떠올리며 추가

# <풀이 연습 과정>
num = 10
x = [int(a) for a in str(num)]
sum_x = sum(x)
# new_x = ''.join(x)
new_x = ''.join(map(str, x))
new_x = int(new_x)
print('new x: ', new_x)

print('type x: ', type(x))
print('type sum_x: ', type(sum_x))
print('type new_x: ', type(new_x))
print(x)
print(sum_x)

## 두 번째 맞는 풀이
def solution(x):
    x = [int(i) for i in str(x)]
    sum_x = sum(x)
    new_x = ''.join(map(str, x))
    new_x = int(new_x)

    if new_x % sum_x:
        answer = False
    else:
        answer = True

    return answer

## 다른 사람 코드
def solution1(x):
    
    # n은 하샤드 수인가요?
    
    """
    해당 코드는 x를 sum으로 바로 나눠서 true와 false를 return 해주는 코드입니다.
    sum 해주는 코드 안에는 정수로 입력된 x를 문자열로 바꿔주는데
    그 이유는 각 자릿수를 더하기 위함입니다.
    그리고 더하기 위해선 int로 변환되어야 해서 int(c)로 사용되었습니다.
    """
    
    return x % sum([int(c) for c in str(x)]) == 0

## 다른 사람 코드 2
def solution2(x):
    
    st = str(x)
    a = 0
    
    for i in range(len(st)):
        a += int(st[i])
        
    return True if x % a == 0 else False