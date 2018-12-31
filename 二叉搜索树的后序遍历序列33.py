# -*- coding:utf-8 -*-
'''
32 后序遍历：LRV
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence)==0:
            return False
        root=sequence[-1]
        #左子树都小于root，右子树都大于root，根据这个分割
        for i in range(len(sequence)):
            if sequence[i]>root:
                break
        for j in range(i,len(sequence)):
            if sequence[j]<root:
                return False
        #先验证左子树是否满足规则，再验证右子树，都对了就返回True
        left=True
        if i>0:
            left=self.VerifySquenceOfBST(sequence[0:i])
        right=True
        if left and len(sequence)-i>1:
            right=self.VerifySquenceOfBST(sequence[i:-1])
        return right

    def VerifySquenceOfPST(self, sequence):
        # write code here
        if len(sequence)==0:
            return False
        root=sequence[0]
        #左子树都小于root，右子树都大于root，根据这个分割
        for i in range(1,len(sequence)):
            if sequence[i]>root:
                break
        for j in range(i+1,len(sequence)):
            if sequence[j]<root:
                return False
        #先验证左子树是否满足规则，再验证右子树，都对了就返回True
        left=True
        if i>0:
            left=self.VerifySquenceOfPST(sequence[1:i])
        right=True
        if left and len(sequence)>i-1:
            right=self.VerifySquenceOfPST(sequence[i+1:])
        return right

def main():
    sol=Solution()
    pre = [5,3,2,1,4,7,6,8]
    tin = [4,7,2,1,5,3,8,6]
    post= [1,2,4,3,6,8,7,5]
    veryBST = sol.VerifySquenceOfBST(post)
    veryPST = sol.VerifySquenceOfPST(pre)
    #newTree2 = sol.reConstructBinaryTree2(post, tin)
    #print(veryBST)
    print(veryPST)

if __name__ == '__main__':
    main()

