# 539. Minimum Time Difference

# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
# Example 1:
#
# Input: ["23:59","00:00"]
# Output: 1

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = []
        result = 90000000

        for tp in timePoints:
            stp = tp.split(":")
            if int(stp[0]) < 12:
                if [int(stp[0]) + 24, int(stp[1])] not in time:
                    time.append([int(stp[0]) + 24, int(stp[1])])

            time.append([int(stp[0]), int(stp[1])])

        time = sorted(time, key=lambda x: (x[0], x[1]), reverse=True)

        for i in range(0, len(time) - 1):
            newT1 = time[i]
            newT2 = time[i + 1]

            if newT1[1] < newT2[1]:
                newT1[0] -= 1
                newT1[1] += 60

            result = min(result, newT1[1] - newT2[1] + (newT1[0] - newT2[0]) * 60)

        return result


