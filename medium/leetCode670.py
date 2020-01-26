# 670. Maximum Swap
#
#
# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.
#
# Example 1:
#
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
#
# Input: 9973
# Output: 9973
# Explanation: No swap.


import heapq


class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        initial = max(digits)
        queue = []

        if digits.index(initial) != 0:
            if digits.count(initial) != 1:
                for i in range(len(digits) - 1, -1, -1):
                    if digits[i] == initial:
                        idx = i
                        break
            else:
                idx = digits.index(initial)
            temp = digits[0]
            digits[0] = initial
            digits[idx] = temp

            return int("".join(digits))

        elif digits.index(initial) == 0:
            seq = 1
            appendFlag = False
            for i in range(1, len(digits)):
                queue.append(digits[i])

            queue.sort(reverse=True)

            while queue:
                print(queue)
                target = queue.pop(0)
                if digits.count(target) != 1:  # 중복된 원소를 한번 거친 경우
                    for i in range(len(digits) - 1, -1, -1):
                        if digits[i] == target:
                            idx = i
                            break
                else:
                    idx = digits.index(target)
                print(idx)
                print(seq)
                if idx != seq and digits[idx] != digits[seq]:
                    temp = digits[seq]
                    digits[seq] = target
                    digits[idx] = temp

                    break

                else:
                    seq += 1

            return int("".join(digits))