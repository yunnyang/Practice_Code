#6. ZigZag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        line = []
        result = ""
        remain = list(s)

        if len(s) == 0:
            return ""
        elif len(s) <= numRows:
            for i in range(0, len(s)):
                line.append([])
                line[i].append(s[i])

            for i in range(0, len(s)):
                temp = "".join(line[i])
                result = result + temp

        else:
            for i in range(0, numRows):
                line.append([])

            while True:
                for i in range(0, numRows):
                    line[i].append(remain[i])

                remain = list(remain[numRows:])

                for i in range(numRows - 2, 0, -1):
                    if len(remain) == 0:
                        break
                    else:
                        line[i].append(remain[0])
                        remain.remove(remain[0])

                if int(len(remain)) <= numRows:
                    for i in range(0, len(remain)):
                        line[i].append(remain[i])
                    break

            for i in range(0, numRows):
                temp = "".join(line[i])
                result = result + temp

        return result
