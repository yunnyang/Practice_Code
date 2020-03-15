# 394. Decode String

class Solution:
    def decodeString(self, s: str) -> str:

        if s == "":
            return ""

        k = ""
        left = 0
        right = 0

        substring = ""
        start = 0

        result = ""

        subStart = 0
        subEnd = 0

        for i in range(len(s)):
            if s[i].isdigit() == True and left == 0:
                k += s[i]


            elif s[i].isalpha() == True and left == 0:
                result += s[i]

            elif s[i] == "[":
                left += 1
                if left == 1:
                    subStart = i + 1
                    # substring = s[i+1:]

            elif s[i] == "]":
                right += 1

                if left == right:
                    k = int(k)
                    subEnd = i
                    substring = s[subStart:subEnd]
                    start = i + 1
                    if "[" not in substring:
                        result += k * substring + self.decodeString(s[start:])
                        break
                    elif "[" in substring:
                        result += k * self.decodeString(substring) + self.decodeString(s[start:])
                        break
                    else:
                        result += k * substring
                        break

        return result