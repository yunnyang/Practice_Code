class Solution:
    def reverseWords(self, s: str) -> str:
        Array = s.split(" ")

        result = ""

        for A in Array:
            result += "".join(A[::-1])
            result += " "

        return result[:len(result) - 1]