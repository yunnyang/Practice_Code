#71 Simplify Path

class Solution:
    def simplifyPath(self, path: str) -> str:
        pathCheck = path
        if list(set(pathCheck))[0] == "/":
            return "/"

        canonical = []

        for p in path.split("/"):
            if p != "":
                if p == "..":
                    if len(canonical) == 0:
                        canonical.append("/")
                    elif len(canonical) >= 2:
                        canonical.pop()
                        canonical.pop()

                elif p == ".":
                    if len(canonical) == 0:
                        canonical.append("/")

                elif p != ".":
                    if len(canonical) != 1:
                        canonical.append("/")
                    canonical.append(p)

        if len(canonical) == 0:
            return "/"

        return str("".join(canonical))