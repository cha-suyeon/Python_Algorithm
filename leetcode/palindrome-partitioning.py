# https://leetcode.com/problems/palindrome-partitioning/
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def isPal(start:int, end: int):
            substring = s[start: end + 1 ]
            return substring == substring[::-1]

        # 선택(append) -> 재귀 호출 -> 복원(pop)
        def backtrack(start, current_partition):
            if start == len(s):
                # result.append(current_partition)
                result.append(list(current_partition))

            for i in range(start, len(s)):
                if isPal(start, i):
                    current_partition.append(s[start:i+1])
                    backtrack(i+1, current_partition)
                    current_partition.pop()
        
        backtrack(0, [])

        return result
    
# --- 실행 예시 ---
solution = Solution()
result_abb = solution.partition("aab")
print(f"Case 'aab': {result_abb}") # 예상 출력: [['a', 'a', 'b'], ['aa', 'b']]

result_abba = solution.partition("abba")
print(f"Case 'abba': {result_abba}") # 예상 출력: [['a', 'b', 'b', 'a'], ['a', 'bb', 'a'], ['abba']]

result_abc = solution.partition("abc")
print(f"Case 'abc': {result_abc}") # 예상 출력: [['a', 'b', 'c']]

result_aabaa = solution.partition("aabaa")
print(f"Case 'aabaa':{result_aabaa}") # 예상 출력: :[['a', 'a', 'b', 'a', 'a'], ['a', 'a', 'b', 'aa'], ['a', 'aba', 'a'], ['aa', 'b', 'a', 'a'], ['aa', 'b', 'aa'], ['aabaa']]

