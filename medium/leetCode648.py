# 648. Replace Words

import collections


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        visited = collections.defaultdict()

        for i in range(len(words)):
            word = words[i]
            if word in visited:
                words[i] = visited[word]
            else:
                for d in dict:
                    if d in word:
                        if word.find(d) == 0:
                            visited[word] = d
                            words[i] = d
                            break

        return " ".join(words)