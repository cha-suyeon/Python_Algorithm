class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for p in s:
            if p == "{":
                stack.append("}")
            elif p == "[":
                stack.append("]")
            elif p == "(":
                stack.append(")")
            elif stack and stack[-1] == p:
                stack.pop()
            else:
                return False
            
        return not stack
        
# --- 실행 예시 ---
solution = Solution()

# # 1. 유효한 경우
example_word_1 = "()[]{}"
result_1 = solution.isValid(example_word_1)
print(f"'{example_word_1}' is valid: {result_1}")  # 예상 출력: True
print("\n-----------\n")

# # 2. 유효하지 않은 경우
example_word_2 = "(]"
result_2 = solution.isValid(example_word_2)
print(f"'{example_word_2}' is valid: {result_2}")  # 예상 출력: False
print("\n-----------\n")

# # 3. 여는 괄호가 남는 경우
example_word_3 = "([{"
result_3 = solution.isValid(example_word_3)
print(f"'{example_word_3}' is valid: {result_3}")  # 예상 출력: False
print("\n-----------\n")

# 4. 빈 문자열의 경우
example_word_4 = ""
result_4 = solution.isValid(example_word_4)
print(f"'{example_word_4}' is valid: {result_4}") # 예상 출력: True