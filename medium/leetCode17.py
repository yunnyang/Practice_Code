# 17. Letter Combinations of a Phone Number


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_letter = {'1': [''],
                        '2': ['a', 'b', 'c'],
                        '3': ['d', 'e', 'f'],
                        '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'],
                        '6': ['m', 'n', 'o'],
                        '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'],
                        '9': ['w', 'x', 'y', 'z'],
                        '0': [' ']}

        letter = []
        x = len(digits)
        if x == 0:
            return []
        elif x == 1:
            return phone_letter[digits]
        else:
            letter = phone_letter[digits[0]]
            for digit in digits[1:]:
                tmp = []
                for i in letter:
                    for j in phone_letter[digit]:
                        tmp.append(i + j)
                letter = tmp
            return letter

