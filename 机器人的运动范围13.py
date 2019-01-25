# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        visited=[[0 for i in range(cols)] for j in range(rows)]
        print(visited)
        x=self.step(0,0,visited,threshold,rows,cols)
        return x

    def getDigit(self,x):
        num=0
        while x!=0:
            num+=x%10
            x/=10
        return num

    def judge(self,x,y,threshold,rows,cols,visited):
        #print(x,y)
        if x>=0 and x<rows and y>=0 and y<cols and self.getDigit(x)+self.getDigit(y)<=threshold:
            #print(x,y)
            if visited[x][y]==0:
                return True
        return False


    def step(self,i,j,visited,threshold,rows,cols):
        #超出边界，或者已经遍历过，或者超出了阈值
        count=0
        if self.judge(i,j,threshold,rows,cols,visited):
            #print(count)
            visited[i][j]=1
            count=1+self.step(i-1,j,visited,threshold,rows,cols)+self.step(i+1,j,visited,threshold,rows,cols)+\
                   self.step(i,j-1,visited,threshold,rows,cols)+self.step(i,j+1,visited,threshold,rows,cols)
        return count

if __name__ == "__main__":
    a = Solution()
    print(a.movingCount(5,10,10))