from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_found = None # 정답을 담을 변수 (None으로 초기화)

        def backtracking(start, current_combination):
            nonlocal result_found

            # 가지치기: 이미 답을 찾았으면 더 탐색할 필요 없음
            if result_found is not None:
                return

            # 1. 종료 조건(Base Case) 수정: current_combination의 길이를 확인
            if len(current_combination) == 2:
                idx1 = current_combination[0]
                idx2 = current_combination[1]
                if nums[idx1] + nums[idx2] == target:
                    result_found = current_combination[:] # 정답을 복사해서 저장
                return
            
            # start 값이 배열의 범위를 벗어나면 더 이상 탐색 불가
            if start >= len(nums):
                return

            # for 루프로 조합 생성
            for i in range(start, len(nums)):
                current_combination.append(i) # 선택
                backtracking(i + 1, current_combination) # 탐색
                current_combination.pop() # 선택 취소 (백트래킹)

        initial_combination = []
        backtracking(0, initial_combination)
        
        # 2. 최종 결과 반환
        return result_found

# --- 실행 예시 ---
solver = Solution()
nums_example = [3, 2, 4]
target_example = 6
final_answer = solver.twoSum(nums_example, target_example)
print(f"최종 결과: {final_answer}") # 최종 결과: [1, 2]