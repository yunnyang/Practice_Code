# 49. Group Anagrams

import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = dict()

        for s in strs:
            temp = list(s[:])
            temp.sort()

            if "".join(temp) in anagram.keys():
                anagram["".join(temp)].append(s)

            else:
                anagram["".join(temp)] = [s]

        anagram = list(anagram.items())

        anagram = [x[1] for x in anagram]

        return anagram