N = int(input())

room = []
for i in range(N):
    room.append(list(map(str, input())))

horizontal = 0
vertical = 0

for i in range(N):
    row_count = 0
    col_count = 0

    for j in range(N):
        if room[i][j] == '.':
            row_count += 1
        else:
            if row_count >= 2:
                horizontal += 1
            row_count = 0

        if room[j][i] == '.':
            col_count += 1
        else:
            if col_count >= 2:
                vertical += 1
            col_count = 0

    if row_count >= 2:
        horizontal += 1
    if col_count >= 2:
        vertical += 1
        
print(horizontal, vertical)