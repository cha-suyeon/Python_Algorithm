from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 # 0, 5
        print(f"First Left: {l}, Right: {r}")
        count = 0
        while l <= r: # True인 동안 도니까
            print(f"Count: {count}")
            mid = (l+r) // 2
            print(f"Midlle: {mid}")
            if target > nums[mid]: # 중앙값보다 크면
                l = mid + 1
                print(f"Left: {l}")
                
            elif target < nums[mid]: # 중앙값보다 작으면
                r = mid - 1
                print(f"Right: {r}")
            else:
                return mid # 인덱스 반환
            count += 1
            

# --- 실행 예시 ---
nums = [2, 6, 9, 14, 15, 17, 19, 22, 25, 26, 37, 45, 58, 67, 82]
solution = Solution()
result = solution.search(nums, 58)
print(f"\n최종 결과: {result}")
