# 순열
def permute(nums):
    def backtrack(curr):
        if len(curr) == len(nums):
            result.append(curr[:])
            return

        for num in nums:
            curr.append(num)
            backtrack(curr)
            curr.pop()
    
    result = []
    backtrack([])
    return result

# --- 실행 예시 ---
nums_example = [1, 2, 3]
all_permutations = permute(nums_example)
print(f"입력: nums = {nums_example}\n")
print(f"모든 순열: {all_permutations}")
print(f"순열의 개수: {len(all_permutations)}")
print(f"기대 개수 (3! = 6): {3*2*1}")