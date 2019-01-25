class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        dict = {}
        for num in numbers:
            dict[num] = 1 if num not in dict else dict[num]+1
            if dict[num] > len(numbers)/2:
                return num
        return 0