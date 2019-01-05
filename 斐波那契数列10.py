# fib
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0:
            return 0
        if n<=2 and n>0:
            return 1
        i=0
        j=1
        fib=0
        k=2
        while k<=n:
            fib=i+j
            tmp=j
            j=j+i
            i=tmp
            k+=1
        return fib

#跳台阶
#z=x+y; n=2x+y; 跳法：z!/(z-x)!x!
class Solution:
    def jumpFloor(self, number):
        # write code here
        n=number
        def fac(m):
            res=1
            for i in range(1,m+1):
                res*=i
            return res
        res=0
        for x in range(n/2+1):
            res+=fac(n-x)/(fac(n-2*x)*fac(x))
        return res

# fib(n)=fib(n-1)+fib(n-2)
    def jumpFloor2(self, number):
        n=number
        if n<=2:
            return n
        pre,curr=1,2
        for _ in range(3,n+1):
            pre,curr=curr,pre+curr
        return curr

