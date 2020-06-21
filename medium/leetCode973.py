class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def getDistance(x, y):
            return x ** 2 + y ** 2

        pointDistance = dict()

        for x, y in points:
            pointDistance[(x, y)] = getDistance(x, y)

        sortDistance = sorted(pointDistance.items(), key=lambda x: x[1])

        answer = [x[0] for x in sortDistance]

        return answer[:K]