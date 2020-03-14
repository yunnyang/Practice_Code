# 365. Water and Jug Problem

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:

        Max = max(x, y)
        Min = min(x, y)

        x = Min
        y = Max

        if z == 0:
            return True

        if x == z or y == z:
            return True

        if x == y and x != z:
            return False

        queue = collections.deque()
        visited = set()

        queue.append((x, 0))
        queue.append(((0, y)))
        while queue:
            a, b = queue.popleft()
            if a == z or b == z:
                return True


            elif a >= 0 and b >= 0:
                if a == 0:
                    if x + b == z:
                        return True

                    if x < b - x:
                        if (0, b - x) not in visited:
                            visited.add((0, b - x))
                            queue.append((0, b - x))

                    if b + x < y:
                        if (0, b + x) not in visited:
                            visited.add((0, b + x))
                            queue.append((0, b + x))

                    if x > y - b:
                        if x - (y - b) not in visited:
                            visited.add((x - (y - b), 0))
                            queue.append((x - (y - b), 0))

                    if b - x < x:
                        if (b - x, 0) not in visited:
                            visited.add((b - x, 0))
                            queue.append((b - x, 0))

                if b == 0:
                    if a + y == 0:
                        return True

                    if (0, a) not in visited:
                        visited.add((0, a))
                        queue.append((0, a))

                    if (0, y - (x - a)) not in visited:
                        visited.add((0, y - (x - a)))
                        queue.append((0, y - (x - a)))
        return False