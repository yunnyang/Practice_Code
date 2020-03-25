# 165. Compare Version Numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        if version1 == version2:
            return 0

        if len(version1) == 0:
            version1 = "0"

        if len(version2) == 0:
            version2 = "0"

        ver1 = version1.split(".")
        ver2 = version2.split(".")

        while ver1 and ver2:
            v1 = int(ver1.pop(0))
            v2 = int(ver2.pop(0))

            if v1 > v2:
                return 1

            elif v1 < v2:
                return -1

        if len(ver1) == 0 and len(ver2) == 0:
            return 0

        elif len(ver1) != 0 and len(ver2) == 0:
            for v in ver1:
                if int(v) is not 0:
                    return 1

            return 0

        elif len(ver1) == 0 and len(ver2) != 0:
            for v in ver2:
                if int(v) is not 0:
                    return -1

            return 0