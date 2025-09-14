from collections import deque

def solution(queue1, queue2):
    answer = 0
    dequeue1 = deque(queue1)
    sum1 = sum(dequeue1)
    dequeue2 = deque(queue2)
    sum2 = sum(dequeue2)
    target = (sum1 + sum2) / 2

    if target != int(target):
        return -1
    
    limit = len(queue1) * 3
    
    while sum1 != target: 
        if answer > limit:
            return -1
    
        answer += 1
        
        if sum1 > target:
            q1_left = dequeue1.popleft()
            dequeue2.append(q1_left)
            sum1 = sum1 - q1_left
            sum2 = sum2 + q1_left
        elif sum1 < target:
            q2_left = dequeue2.popleft()
            dequeue1.append(q2_left)
            sum1 = sum1 + q2_left
            sum2 = sum2 - q2_left
            
    return answer

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
print(solution(queue1, queue2))
