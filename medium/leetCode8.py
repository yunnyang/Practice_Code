# 8. String to Integer (atoi)
#
# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.split(" ")
        line = []
        count = 0
        flag = 0
        for i in range(0, len(s)):
            if s[i] != "":
                line = s[i]
                break

        if line == []:
            return 0

        for i in range(0, len(line)):
            if line[i] != "+" and line[i] != "-" and line[i].isdecimal() == False:
                break
            else:
                if line[i].isdecimal() == True:
                    flag = 1 #if num appear, then +/- shoud be discarede.
                if flag == 1 and (line[i] == "+" or line[i] == "-"):
                    break
                count = count + 1

        line = line[:count]

        if line.isnumeric() == False:
            result = 0
            try:
                result = int(line)

            except:
                try:
                    result = float(line)
                    result = int(result)

                except:
                    result = 0
            finally:

                if result >= 2147483647:
                    result = 2147483647
                elif result <= -2147483648:
                    result = -2147483648

                return result


        else:
            if int(line) >= 2147483647:
                return 2147483647
            elif int(line) <= -2147483648:
                return -2147483648
            return int(line)



