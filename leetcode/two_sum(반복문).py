from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        def backtracking(start):
            if len(result) == 2:
                idx1 = result[0]
                idx2 = result[1]
                if nums[idx1] + nums[idx2] == target:
                    return result
                return False

            for i in range(start, len(nums)):
                result.append(i)
                if backtracking(i+1):
                    return result
                result.pop()

        return backtracking(0) # pyright: ignore[reportReturnType]
    
# --- 실행 예시 ---
solver = Solution()
nums_example = [3, 2, 4]
target_example = 6
final_answer = solver.twoSum(nums_example, target_example)
print(f"최종 결과: {final_answer}") # 최종 결과: [1, 2]