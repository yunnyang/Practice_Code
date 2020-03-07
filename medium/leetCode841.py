# 841. Keys and Rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = collections.deque()
        visited = set()

        if len(rooms) == 0:
            return False

        if len(rooms) == 1:
            return True

        stack.append(0)

        while stack:
            target = stack.pop()
            visited.add(target)

            for t in rooms[target]:
                if t not in visited:
                    stack.append(t)

        if len(visited) != len(rooms):
            return False

        else:
            return True




