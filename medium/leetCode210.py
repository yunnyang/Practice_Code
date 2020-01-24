# 210. Course Schedule II

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        if len(prerequisites) == 0:
            return list(range(numCourses - 1, -1, -1))

        indegree, graph = self.builgGraph(prerequisites)
        return self.courseOrder(numCourses, indegree, graph)

    def builgGraph(self, prerequisites):
        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)

        for c1, c2 in prerequisites:
            graph[c2].append(c1)
            indegree[c1] += 1
            if c2 not in indegree:
                indegree[c2] = 0

        return indegree, graph

    def courseOrder(self, numCourses, indegree, graph):
        queue = collections.deque(filter(lambda a: indegree[a] == 0, indegree.keys()))
        order = []

        while queue:
            v = queue.popleft()
            order.append(v)
            for neighbor in graph[v]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) == numCourses:
            return order

        if len(order) != len(indegree):
            return []
        else:
            return self.findCourse(numCourses, order)

    def findCourse(self, numCourses, order):
        if len(order) == 0:
            return []

        for i in range(0, numCourses):
            if i not in order:
                order.insert(0, i)

        return order