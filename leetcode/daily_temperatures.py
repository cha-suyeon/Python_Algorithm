from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        answer = [0] * len(temperatures)
        
        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = idx - prev_index

            stack.append(idx)

        return answer
    
# --- 실행 예시 ---
solution = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
answer = solution.dailyTemperatures(temperatures)
print(answer)