#937. Reorder Data in Log Files

# (1) divide logs with identifier
# (2) order letter logs by lexicographically ignoring identifier
# (3) combine letter logs and digit logs

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = list()
        words = dict()
        result = list()

        # (1) divide logs with identifier
        for log in logs:
            temp = log.split(" ")

            idf = temp[1:][0]

            if idf.isdigit() is False:
                letters.append(log)

        # (2) order letter logs by lexicographically ignoring identifier
        letters.sort()

        for letter in letters:
            logs.remove(letter)

            temp = letter
            temp = temp.split(" ")[1:]

            words[letter] = temp

        words = sorted(words.items(), key=lambda x: x[1])

        # (3) combine letter logs and digit logs
        for word in words:
            result.append(word[0])

        for log in logs:
            result.append(log)
        return result

