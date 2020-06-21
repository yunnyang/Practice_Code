# 692. Top K Frequent Words

# Your answer should be sorted by frequency from highest to lowest.
# If two words have the same frequency, then the word with the lower alphabetical order comes first.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        count = collections.Counter(words)
        output = sorted(count.keys(), key=lambda w:count[w],reverse = True)
        return output[:k]