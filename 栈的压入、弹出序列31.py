class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        res=False
        substack = []
        for i in pushV:
            substack.append(i)
            #判断是否需要出栈
            while substack and substack[-1]==popV[0]:
                substack.pop()
                #print(popV)
                popV.pop(0)
            #print(substack)
        if not substack:
            res=True
        return res

def main():
    pushV=[1,2,3,4,5]
    popV=[1,2,3,4,5]
    sol=Solution()
    res=sol.IsPopOrder(pushV,popV)
    print(res)

if __name__ == '__main__':
    main()