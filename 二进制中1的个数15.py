class Solution:
    def NumberOf1(self, n):
        # write code here
        cnt = 0
        #负数
        if n < 0:
            n = n & 0xffffffff
        while n:
            n =  n & (n - 1)
            cnt += 1
        print(n)
        return cnt

if __name__ == "__main__":
    a = Solution()
    print(a.NumberOf1(5))