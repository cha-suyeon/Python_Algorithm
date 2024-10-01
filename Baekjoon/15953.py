# 1
def calculate_prize(a, b):
    price_17 = 0
    price_18 = 0

    if a == 1:
        price_17 += 5000000
    elif 1 < a <= 3:
        price_17 += 3000000
    elif 3 < a <= 6:
        price_17 += 2000000
    elif 6 < a <= 10:
        price_17 += 500000
    elif 10 < a <= 15:
        price_17 += 300000
    elif 15 < a <= 21:
        price_17 += 100000
    else:
        price_17 = 0

    if b == 1:
        price_18 += 5120000
    elif 1 < b <= 3:
        price_18 += 2560000
    elif 3 < b <= 7:
        price_18 += 1280000
    elif 7 < b <= 15:
        price_18 += 640000
    elif 15 < b <= 31:
        price_18 += 320000
    else:
        price_18 = 0

    return price_17 + price_18

T = int(input())    
for _ in range(T):
    a, b = map(int, input().split(' '))
    result = calculate_prize(a,b)
    print(result)

# 2
prizes_2017 = [0, 5000000, 3000000, 3000000, 2000000, 2000000, 2000000, 500000, 500000, 500000, 500000,
               300000, 300000, 300000, 300000, 300000, 100000, 100000, 100000, 100000, 100000, 100000]
prizes_2018 = [0, 5120000, 2560000, 2560000, 1280000, 1280000, 1280000, 1280000, 640000, 640000, 640000, 640000,
               640000, 640000, 640000, 640000, 320000, 320000, 320000, 320000, 320000, 320000, 320000, 320000, 
               320000, 320000, 320000, 320000, 320000, 320000, 320000, 320000]

def calculate_prize(a, b):
    prize_17 = prizes_2017[a] if a <= 21 else 0
    prize_18 = prizes_2018[b] if b <= 31 else 0
    return prize_17 + prize_18

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(calculate_prize(a, b))


# 3
prizes_2017 = [0, 5000000, 3000000, 3000000, 2000000, 2000000, 2000000, 500000, 500000, 500000, 500000,
               300000, 300000, 300000, 300000, 300000, 100000, 100000, 100000, 100000, 100000, 100000]
prizes_2018 = [0, 5120000, 2560000, 2560000, 1280000, 1280000, 1280000, 1280000, 640000, 640000, 640000, 640000,
               640000, 640000, 640000, 640000, 320000, 320000, 320000, 320000, 320000, 320000, 320000, 320000, 
               320000, 320000, 320000, 320000, 320000, 320000, 320000, 320000]

def calculate_prize(a, b):
    prize_17 = prizes_2017[a] if a <= 21 else 0
    prize_18 = prizes_2018[b] if b <= 31 else 0
    return prize_17 + prize_18

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(calculate_prize(a, b))
