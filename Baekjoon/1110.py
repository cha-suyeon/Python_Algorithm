current = int(input())

initial = current
cycle = 0

while True:
    current_sum = current // 10 + current % 10
    next_sum = (current % 10) * 10 + (current_sum % 10)
    cycle += 1

    if next_sum == initial:
        break
    
    current = next_sum

print(cycle)