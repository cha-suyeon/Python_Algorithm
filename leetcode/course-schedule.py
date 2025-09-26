from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 제공해주신 topological_sort 로직을 그대로 사용합니다.
        
        # 1. 그래프 및 진입 차수 배열 초기화
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        # 2. 그래프 구성 및 진입 차수 계산
        # 문제의 입력은 [a, b]가 b -> a 를 의미합니다.
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
            
        # 3. 진입 차수가 0인 노드를 큐에 추가
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                
        # 위상 정렬을 통해 수강한 과목 수를 카운트
        finished_courses = 0
        
        # 4. 큐가 빌 때까지 반복
        while q:
            cur_course = q.popleft()
            finished_courses += 1
            
            for next_course in graph[cur_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
                    
        # 5. 수강 완료한 과목 수가 전체 과목 수와 같으면 True, 아니면 False 반환
        return finished_courses == numCourses