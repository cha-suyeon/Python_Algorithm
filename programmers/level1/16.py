# 2016년

## 나의 풀이
import datetime

def solution(a, b):
    answer = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    n = datetime.datetime(2016, a, b).weekday()
    return answer[n]

## 남의 풀이 1
def solution1(a,b):
    months = [31,29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

## 남의 풀이 2
def solution2(a,b):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    dayLen = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    now = 5
    
    for i in range(0, a-1): # range가 0부터 a-1까지
        now += dayLen[i]
        
    answer = (now + b - 1) % 7
    
    return days[answer]

## 남의 풀이 3
def solution3(a,b):
    day_name = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month_dict = {
        "1":31, 
        "2":29, 
        "3":31, 
        "4":30, 
        "5":31, 
        "6":30, 
        "7":31, 
        "8":31, 
        "9":30, 
        "10":31, 
        "11":30, 
        "12":31
    }
    days = 0
    
    for i in range(1, a): # range로 1부터 a까지 (실제로는 1, ..., a-1)
        days += month_dict[str(i)]
    days += b
    index = days % 7
    
    return day_name[index]

print(solution3(5,24))