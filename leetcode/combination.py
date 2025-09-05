# 조합
def combination(nums, k):
    def backtrack(curr, start):
        if len(curr) == k:
            result.append(curr[:])
            return
        
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(curr, i+1)
            curr.pop()

    result = []
    backtrack([], 1)
    return result

# --- 실행 예시 ---
nums = [1, 2, 3, 4]
k = 2
print(f"입력: nums = {nums}, k = {k}\n")
all_combinations = combination(nums, k)
print(f"모든 조합: {all_combinations}")
print(f"조합의 개수: {len(all_combinations)}")
print(f"기대 개수 (4C2 = 6): {4*3//2}")  # 4C2 계산