# 139. Word Break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        stack = collections.deque()
        stack.append(s)
        visited = set()
        while stack:
            target = stack.pop()

            if len(target) == 0:
                return True

            for word in wordDict:
                if len(target) >= len(word):
                    if word == target[:len(word)]:
                        if target[len(word):] not in visited:
                            stack.append(target[len(word):])
                            visited.add(target[len(word):])

        return False

