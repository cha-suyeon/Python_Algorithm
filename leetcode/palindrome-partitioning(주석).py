# https://leetcode.com/problems/palindrome-partitioning/
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        print(f"Target word: {s}")
        # 팰린드롬 확인 헬퍼 함수
        def isPal(start: int, end: int):
            # start부터 end까지의 부분 문자열을
            # 올바른 슬라이싱 문법으로 추출하고
            # 팰린드롬인지 판단하여 True/False 반환하기
            # (예: s[start:end+1] == s[start:end+1][::-1])
            return s[start:end] == s[start:end][::-1]
        
        def backtrack(start, current_partition):
            # 1. 종료 조건 (Base Case):
            #    start가 문자열의 길이(len(s))와 같아지면, 모든 문자를 분할했다는 뜻이므로
            #    result에 current_partition의 복사본을 추가하고 함수를 종료합니다.
            if start == len(s):
                result.append(list(current_partition))

            # 2. 반복문: 현재 위치(start)부터 문자열 끝까지 탐색
            for i in range(start, len(s)):
                # 3. 팰린드롬인지 확인:
                #    isPal 함수를 이용해 s[start]부터 s[i]까지의 부분 문자열이 팰린드롬인지 확인합니다.
                if isPal(start, i):
                    current_partition.append(s[start:i+1])
                    print(f"s => {s[start:i+1]}")
                    print(f"Index number => Start: {start}, end: {i+1}")
                    backtrack(i+1, current_partition)
                    current_partition.pop()
                # 4. 만약 팰린드롬이라면:
                #    a. 선택: 현재 찾은 팰린드롬을 current_partition에 추가합니다.
                #    b. 재귀 호출: 다음 시작점(i+1)으로 backtrack 함수를 호출합니다.
                #    c. 복원: 재귀 호출이 끝난 후, current_partition에서 방금 추가한 것을 제거하여 이전 상태로 되돌립니다.

        # 5. 백트래킹 시작:
        #    첫 호출은 start를 0으로, current_partition을 빈 리스트로 시작합니다.
        backtrack(0, [])

        return result    
    
    
# --- 실행 예시 ---
solution = Solution()
result_abb = solution.partition("aab")
print(f"Case 'aab': {result_abb}") # 예상 출력: [['a', 'a', 'b'], ['aa', 'b']]

# result_abba = solution.partition("abba")
# print(f"Case 'abba': {result_abba}") # 예상 출력: [['a', 'b', 'b', 'a'], ['a', 'bb', 'a'], ['abba']]

# result_abc = solution.partition("abc")
# print(f"Case 'abc': {result_abc}") # 예상 출력: [['a', 'b', 'c']]

# result_aabaa = solution.partition("aabaa")
# print(f"Case 'aabaa':{result_aabaa}") # 예상 출력: :[['a', 'a', 'b', 'a', 'a'], ['a', 'a', 'b', 'aa'], ['a', 'aba', 'a'], ['aa', 'b', 'a', 'a'], ['aa', 'b', 'aa'], ['aabaa']]

