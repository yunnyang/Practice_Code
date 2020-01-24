# 630. Course Schedule III


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        day = 0  # day start at the 1st day
        courseTaken = []

        courses.sort(key=lambda x: x[1])

        for t, d in courses:
            heapq.heappush(courseTaken, -t)
            day += t

            if day > d:
                day += heapq.heappop(courseTaken)

        return len(courseTaken)