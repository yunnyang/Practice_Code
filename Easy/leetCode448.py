#448. Find All Numbers Disappeared in an Array

# 주어진 배열의 길이만큼의 정수 범위가 주어질 때
# 주어진 범위에서, 배열에 포함되지 않은 숫자 찾기

#when given integer range which given parameter array length
# in given range, find num what is not contained to array

class Solution:
    def findDisappearedNumbers(self, nums) :
        result = []
        numSet = set(nums)
        for i in range(1,len(nums)+1) :
            if i not in numSet :
                result.append(i)
        return result