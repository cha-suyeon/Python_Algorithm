from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                print(f"Fount Target! => Target: {target}, Current Mid: {nums[mid]}")
                return mid
        print("No target in the list")
        return -1
            
# --- 실행 예시 ---
nums = [2, 6, 9, 14, 15, 17, 19, 22, 25, 26, 37, 45, 58, 67, 82]
solution = Solution()
result = solution.search(nums, 58)
print(f"\n최종 결과: {result}")
