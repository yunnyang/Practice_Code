#5. Longest Palindromic Substring
# This code trigger time limit exceeded and Memory limit exceeded

class Solution:
    cache = dict()

    def longestPalindrome(self, s: str) -> str:
        parlindrome = []

        for i in range(0, len(s)):
            longest = []
            for j in range(i, len(s)):
                longest.append(s[j])
                if self.checkPalindrome(longest) == True:
                    if len(longest) == len(s):
                        return ''.join(longest)

                    parlindrome.append(''.join(longest))

        result = ""
        for p in parlindrome:
            if len(p) >= len(result):
                result = p

        return result

    def checkPalindrome(self, s: str) -> str:
        key = str(s)

        if len(set(s)) == 1:
            self.cache[key] = True
            return True

        if key in self.cache:
            return self.cache[key]

        else:
            for i in range(0, int(len(s) / 2)):
                if s[i] != s[~i]:
                    self.cache[key] = False
                    return False

            self.cache[key] = True
            return True