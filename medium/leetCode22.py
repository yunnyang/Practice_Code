# 22. Generate Parentheses
#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

import itertools


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        if n < 1:
            return []

        def inner(comb, a, b):
            if b < a:
                return
            if a == 0:
                out.append(comb + ')' * b)
                return
            inner(comb + '(', a - 1, b)
            inner(comb + ')', a, b - 1)

        inner('', n, n)
        return out