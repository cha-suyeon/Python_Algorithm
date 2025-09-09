from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        indices_num = [(num, i) for i, num in enumerate(nums)]
        indices_num.sort()

        while l < r:
            curr_sum = indices_num[l][0] + indices_num[r][0]
            if curr_sum == target:
                return [indices_num[l][1], indices_num[r][1]]
            elif curr_sum > target:
                r -= 1
            else:
                l += 1

        return False
    
solver = Solution()
nums_example = [3, 2, 4]
target_example = 6
final_answer = solver.twoSum(nums_example, target_example)
print(f"해시맵 결과: {final_answer}") # 최종 결과: [1, 2]