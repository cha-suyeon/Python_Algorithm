from typing import List

class Solution:
    def twoSum_hashmap(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i, num in enumerate(nums):
            complete = target - num

            if complete in memo:
                return [memo[complete], i]

            memo[num] = i

        return []

solver = Solution()
nums_example = [3, 2, 4]
target_example = 6
final_answer = solver.twoSum_hashmap(nums_example, target_example)
print(f"해시맵 결과: {final_answer}") # 최종 결과: [1, 2]