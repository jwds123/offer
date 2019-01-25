class Solution:
    def Power(self, base, exponent):
        # write code here
        if base > -1e-7 and base < 1e-7:
            return 0
        if exponent==0:
            return 1
        if exponent==1:
            return base
        res=1
        for i in range(abs(exponent)):
            res*=base
        if exponent<0:
            res=1/res
        return res

    def Power1(self, base, exponent):
        if base > -1e-7 and base < 1e-7:
            return 0
        if exponent==0:
            return 1
        if exponent==1:
            return base
        res=1
        exp=abs(exponent)
        res=self.Power1(base,exp>>1)
        res=res*res
        if exponent&1==1:
            res*=base
        if exponent<1:
            res=1/res
        return res

