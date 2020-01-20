#58. Length of Last World

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if s.strip() == "":
            return 0

        string = s.split(" ")

        for i in range(len(string) - 1, -1, -1):
            if string[i] != '':
                return len(string[i])
