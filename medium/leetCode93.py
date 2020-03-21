# 93. Restore IP Addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        stack = collections.deque()
        visited = set()

        stack.append(("", s))

        while stack:
            ip, remain = stack.pop()

            if len(remain) == 0 and ip.count(".") == 3:
                result.append(ip)

            if len(ip) != 0:
                ip += "."

            for i in range(1, 4):
                if len(remain) >= i and ip.count(".") <= 3 and (ip + remain[:i], remain[i:]) not in visited:

                    if int(remain[:i]) >= 0 and int(remain[:i]) <= 255 and not (
                            len(remain[:i]) >= 2 and remain[:i][0] == "0"):
                        stack.append((ip + remain[:i], remain[i:]))
                        visited.add((ip + remain[:i], remain[i:]))

        return result