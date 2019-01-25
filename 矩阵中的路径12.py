class Solution:
    global flag, p, dir
    flag = None
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 四个方向

    def hasPath(self, matrix, rows, cols, path):
        global flag, dir

        # 初始化
        visited=[[0 for j in range(cols)] for i in range(rows)]#标记
        li= [[0 for j in range(cols)] for i in range(rows)]#字符串转为二维列表
        flag=False
        # 字符串转为二维列表
        x,y=0,0
        for i in range(len(matrix)):
            li[x][y]=matrix[i]
            y+=1
            if cols==y:
                x,y=x+1,0
        #print(li)

        for i in range(rows):
            for j in range(cols):
                if path[0]==li[i][j]:
                    #s为起点
                    s=path[0]
                    visited[i][j]=1
                    self.DFS(li,i,j,visited,s,rows,cols,path)
                    if flag==True:
                        return True
                    #叶节点不满足条件，回溯到上一个节点
                    else:
                        visited[i][j]=0
        return False

    def DFS(self,li,x,y,visited,s,rows,cols,path):
        global flag, dir
        '''
        停止的条件！！！
        '''
        if flag == True:  # 剪枝
            return
        #s为已经走过的路径，当s和path一样长时，结束
        if s == path:  # DFS结束条件
            flag = True
            return

        for i in range(len(dir)):
            x_dir=x+dir[i][0]
            y_dir=y+dir[i][1]
            #print(x_dir)

            if x_dir>=0 and y_dir>=0 and x_dir<rows and y_dir<cols and len(s)<len(path) and visited[x_dir][y_dir]==0:
                #判断path中的下一个元素是否在li[][]中
                print(path[len(s)])
                if path[len(s)]!=li[x_dir][y_dir]:
                    continue
                visited[x_dir][y_dir]=1
                s+=li[x_dir][y_dir]

                self.DFS(li,x_dir,y_dir,visited,s,rows,cols,path)

                if flag == True:  # 剪枝
                    return
                #回溯,s去掉最后一个元素
                visited[x_dir][y_dir]=0
                s=s[:-1]
        return




if __name__ == "__main__":
    a = Solution()
    #print(a.hasPath("ABCESFCSADEE", 3, 4, "ABCB"))   # False
    #print(a.hasPath("abcesfcsadee", 3, 4, "bcced"))  # True
    print(a.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS",5,8,"SGGFIECVAASABCEHJIGQEMS"))  # False
