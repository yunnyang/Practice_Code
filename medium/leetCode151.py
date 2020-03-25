# 151. Reverse Words in a String


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")

        while True:
            if '' in words:
                words.remove('')

            else:
                break

        words.reverse()

        return " ".join(words)