# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        '''
        使用二分法。
        :param rotateArray:
        :return:
        '''
        if (not rotateArray) or (len(rotateArray)==0):
            return
        index1=0
        index2=len(rotateArray)-1
        indexMid=index1
        while rotateArray[index1]>=rotateArray[index2]:
            if index2-index1==1:
                indexMid=index2
                break
            indexMid=(index1+index2)/2
            if rotateArray[indexMid]>=rotateArray[index1]:
                index1=indexMid
            elif rotateArray[indexMid]<=rotateArray[index2]:
                index2=indexMid
        return rotateArray[indexMid]