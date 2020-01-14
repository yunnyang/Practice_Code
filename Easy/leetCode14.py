#14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from string import ascii_lowercase


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return strs[0] if strs else ''
        common = []
        for i, w in enumerate(strs[0]):
            for j in range(len(strs)):
                if i >= len(strs[j]):
                    break
                if w != strs[j][i]:
                    break
            else:
                common.append(w)
                continue
            break
        return ''.join(common)
