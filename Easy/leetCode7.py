#7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        line = list(str(x))

        if -2147483648 > x or x > 2147483647:
            return 0

        if line[0] == "-":
            line.append(line[0])
            line.remove(line[0])

        line.reverse()

        if line[0] == "0" and len(line) > 1:
            line.remove(line[0])

        if -2147483648 > int("".join(line)) or int("".join(line)) > 2147483647:
            return 0

        return int("".join(line))