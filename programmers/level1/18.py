# 최대공약수와 최소공배수

def solution(n,m):
    nlist = []
    mlist = []
    
    for i in range(1, n+1):
        # 입력 받은 n에서 나눠서 0이 되는 약수를 nlist에 넣어줍니다.
        if n % i == 0:
            nlist.append(i)
    
    print('n의 약수: ', nlist)
            
    for i in range(1, m+1):
        # 입력 받은 m에서 나눠서 0이 되는 약수를 mlist에 넣어줍니다.
        if m % i == 0:
            mlist.append(i)
    
    print('m의 약수: ', mlist)
        
    maxi = []
    
    for i in nlist:
        # nlist에서 원소 하나씩 뽑아줍니다.
        if i in mlist:
            # mlist에 n의 원소가 있는 경우에 maxi 빈 리스트에 넣어줍니다.
            maxi.append(i)
    
    print('공통 약수:', maxi)
    
    # maxi에서 max 값을 뽑아줍니다.
    maximum = max(maxi) 
    print('최대공약수: ', maximum)
    
    # 최소공배수 = 최대공약수 * n을 최대공약수로 나눈 나머지 * m을 최대공약수로 나눈 나머지
    minimum = int(maximum * (n/maximum) * (m/maximum))
    print(minimum)
    
    answer = [maximum, minimum] # [최대공약수, 최소공배수]
    return answer

print(solution(3, 12))

# n의 약수:  [1, 3]
# m의 약수:  [1, 2, 3, 4, 6, 12]
# 공통 약수: [1, 3]
# 최대공약수:  3
# 12
# [3, 12]

