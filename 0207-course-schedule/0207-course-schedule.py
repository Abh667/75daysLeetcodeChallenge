class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph and indegree array
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Add all courses with indegree 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        completed = 0

        while queue:
            curr = queue.popleft()
            completed += 1

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses