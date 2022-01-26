# 크레인 인형뽑기 게임


## 1 (내가 쓴 코드)
def solution(board, moves):
    basket = []
    answer = 0
    
    for i in moves: # moves = [1,5,3,5,1,2,1,4]
        for j in range(len(board)): # range(0,5)
            
            if board[j][i-1] == 0:
                pass
            else:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                
                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop()
                        basket.pop()
                        answer += 2
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves= [1,5,3,5,1,2,1,4]
print(solution(board, moves))

## 2 (다른 사람 코드)
def solution(board, moves):
    new_board = list(map(list, zip(*board))) # 행, 열 전치
    count = 0
    basket = []
    
    for i in moves:
        for j in range(len(new_board[i-1])):
            if new_board[i-1][j] > 0: # 0보다 클 때만 append
                basket.append(new_board[i-1][j]) # basket에 추가
                new_board[i-1][j] = 0 # 0으로 변경하여 더 이상 안 뽑히게 만듦
                if len(basket) >= 2 and basket[-1] == basket[-2]:
                    count += 2
                    del basket[-2:] # 같은 숫자가 연달아 있으면 basket에서 삭제하고 count 증가
                break # 하나 뽑으면 break
            
    return count

## 3 (다른 사람 코드)
def solution(board, moves):
    answer = 0 # 현재까지 획득한 인형의 개수
    basket_stack = [0] # basket을 구현한 리스트(stack)
    board_stacks = []
    moves_rendered = [i-1 for i in moves] # moves의 각 원소는 세로줄 위치를 의미하므로 인덱스 값 조정
    
    # board를 재구성한 board_stacks 만들기
    for i in range(len(board[0])):
        # 큰 틀의 for: 세로줄 개수 만큼 반복
        # board의 row 개수가 세로줄 개수가 됨
        # 큰 틀이 반복될 때마다 새로운 세로줄 완성
        
        board_stacks.append([]) # 빈 리스트를 세로줄의 모임인 board_stacks에 추가
        
        for j in reversed(range(len(board))):
            # 작은 틀의 for: 가로줄 개수만큼 반복
            # 반복마다 현재 세로줄에 인형(item) 추가
            # 가장 깊은 인형이 board에서 마지막 행에 위치하지만
            # board_stacks의 각 세로줄에서는
            # 스택 의미상 첫 원소이므로 역순으로 탐색
            
            item = board[j][i]
            if item:
                board_stacks[i].append(item)
                print(board_stacks)
            else: break
    
    for move in moves_rendered:
        if board_stacks[move]:
            basket_stack.append(board_stacks[move].pop())
            if basket_stack[-1] == basket_stack[-2]:
                basket_stack.pop()
                basket_stack.pop()
                answer += 2
                
    return answer
