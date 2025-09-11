from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        ans = [0] * len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):
            while stack and  stack[-1][0] < temp:
                prev_day = stack.pop()[0]
                ans[prev_day] = day - prev_day
            stack.append((day, temp))
        
        return ans
    
# --- 실행 예시 ---
solution = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
answer = solution.dailyTemperatures(temperatures)
print(answer)