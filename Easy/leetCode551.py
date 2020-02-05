# 551. Student Attendance Record I
class Solution:
    def checkRecord(self, s: str) -> bool:
        Absent = 0
        Late = 0
        lates = 1  # flag
        for i in range(len(s)):
            if s[i] == "A":
                lates = 0
                Late = 0
                Absent += 1
                if Absent > 1:
                    return False

            elif s[i] == 'L':
                lates = 1
                if lates == 1:
                    Late += 1
                lates = 0

                if Late > 2:
                    return False

            else:
                lates = 0
                Late = 0

        return True