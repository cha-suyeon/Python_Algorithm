from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]

        def in_range(i, j):
            return 0 <= i < n and 0 <= j < m

        def backtrack(i, j, w):
            print(f"Base case: {w}✨!")
            if w == len(word):
                return True
            
            if not in_range(i, j) or visited[i][j] or word[w] != board[i][j]:
                return False
            
            visited[i][j] = True

            res = (
                backtrack(i - 1, j, w+1) or
                backtrack(i + 1, j, w+1) or
                backtrack(i, j - 1, w+1) or
                backtrack(i, j + 1, w+1) 
            )

            visited[i][j] = False

            return res

        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0):
                    return True

        return False

# --- 실행 예시 ---
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
# word = "SEE"
word = "FCEA" # False
solution = Solution()
print(f"Result for '{word}': {solution.exist(board, word)}")
