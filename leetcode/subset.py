def subsets(nums):
    def backtrack(curr, start):
        result.append(curr[:])

        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(curr, i+1)
            curr.pop()

    result = []
    backtrack([], 0)
    return result

# --- 실행 예시 ---
nums_subset = [1, 2, 3]
all_subsets = subsets(nums_subset)
print(f"\n입력: nums = {nums_subset}")
print(f"모든 부분집합: {all_subsets}")
print(f"부분집합의 개수: {len(all_subsets)}")
print(f"기대 개수 (2^3 = 8): {2**len(nums_subset)}")