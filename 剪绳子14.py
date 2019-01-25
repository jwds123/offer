class Solution:
    def maxProductAfterCutting(self, n):
        # write code here
        if n<2:
            return 0
        elif n==2:
            return 1
        elif n==3:
            return 2

        max_li=[0,1,2]
        for i in range(3,n+1):
            max=0
            #j=1,2...[i/2]; i-j>=j 寻找max(f(j)*f(i-j))
            for j in range(1,i//2+1):
                tmp=max_li[j]*max_li[i-j]
                if max<tmp:
                    max=tmp
            max_li.append(max)
        return max_li[n]

if __name__ == "__main__":
    a = Solution()
    print(a.maxProductAfterCutting(10))