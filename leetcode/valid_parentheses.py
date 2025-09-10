class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for word in s:
            if word == "(" or word == "{" or word == "[":
                stack.append(word)

            elif word == ")" or word == "}" or word == "]":
                if not stack: 
                    return False
                
                open_word  = stack.pop()


                if word == ")" and open_word != "(":
                    return False
                
                elif word == "}" and open_word != "{":
                    return False
                
                elif word == "]" and open_word != "[":
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