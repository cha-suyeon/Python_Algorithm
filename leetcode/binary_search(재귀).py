from typing import List

class Solution:
    def search(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l > r:
            return -1
        mid = (l + r) // 2
        if target > nums[mid]:
            return self.search(nums, target, mid + 1, r)
        elif target < nums[mid]:
            return self.search(nums, target, l, mid - 1)
        else:
            return mid

# --- 실행 예시 ---
nums = [2, 6, 9, 14, 15, 17, 19, 22, 25, 26, 37, 45, 58, 67, 82]
solution = Solution()

# target이 있는 경우
result_found = solution.search(nums, 58, 0, len(nums) - 1)
print(f"\n최종 결과 (58): {result_found}")

print("-" * 20)

# target이 없는 경우
result_not_found = solution.search(nums, 100, 0, len(nums) - 1)
print(f"\n최종 결과 (100): {result_not_found}")