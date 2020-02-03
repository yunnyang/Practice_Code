# 451. Sort Characters By Frequency
#
# Given a string, sort it in decreasing order based on the frequency of characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.


class Solution:
    def frequencySort(self, s: str) -> str:
        word = list(s)
        seq = dict()

        for w in word:
            if w in seq:
                new = seq[w]
                seq[w] = new + 1

            else:
                seq[w] = 1

        letters = sorted(seq.items(), key=lambda x: x[1], reverse=True)
        text = ""
        for i in range(len(letters)):
            text += letters[i][0] * letters[i][1]

        return text

