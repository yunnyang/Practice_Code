# 735. Asteroid Collision


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        return self.asteroidCollisionHelper(asteroids)

    def asteroidCollisionHelper(self, asteroids: List[int]) -> List[int]:
        result = asteroids

        for i in range(0, len(result) - 1):
            if self.isCollide(result[i], result[i + 1]) == True:
                if result[i] + result[i + 1] == 0:
                    result.pop(i)
                    result.pop(i)

                else:
                    if abs(result[i]) > abs(result[i + 1]):
                        result.pop(i + 1)
                    else:
                        result.pop(i)

                return self.asteroidCollisionHelper(result)
            else:
                i = i + 1

        return result

    def isCollide(self, a, b) -> bool:
        if a * b > 0:
            return False
        else:
            if a > b:  # + -
                return True
            else:
                return False
