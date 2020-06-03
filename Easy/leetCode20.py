# 20. Valid Parentheses
#
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

import collections


class Solution:
    def isValid(self, s: str) -> bool:
        left = collections.deque()
        right = dict()

        right[')'] = '('
        right['}'] = '{'
        right[']'] = '['

        for p in s:
            if p == '(' or p == '{' or p == '[':
                left.append(p)

            else:
                if len(left) == 0:
                    return False

                else:
                    if right[p] == left[-1]:
                        left.pop()

                    else:
                        return False

        if len(left) == 0:
            return True
        else:
            return False

