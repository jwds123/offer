'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array[0]) == 0:
            return False
        rows = 0
        cols = len(array[0]) - 1
        while cols >= -1 and rows <= len(array) - 1:
            if target < array[rows][cols]:
                cols -= 1
            elif target > array[rows][cols]:
                rows += 1
            elif target == array[rows][cols]:
                return True

        return False