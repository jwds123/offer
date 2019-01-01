#方法1：螺旋访问数组
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        out = []
        # m, n分别表示行、列数
        m = len(matrix)
        if m == 0:
            return out

        n = len(matrix[0])
        # 表示访问到第几行第几列了(0,n-1)(0,m-1)
        r = 0
        c = -1
        # cum,rnum分别表示访问列和行元素的限制个数
        cnum = n
        rnum = m - 1

        while cnum >= 0 and rnum >= 0 and len(out) < m * n:
            # 访问一圈：4个方向
            # 从左到右
            for i in range(cnum):
                c += 1
                out.append(matrix[r][c])
            cnum -= 1
            # 从上到下
            for j in range(rnum):
                r += 1
                out.append(matrix[r][c])
            rnum -= 1
            # 从右到左:可能限制还没小于0但out已经满了，所以需要加上该限制条件
            if cnum >= 0 and len(out) < m * n:
                for i in range(cnum):
                    c -= 1
                    out.append(matrix[r][c])
                cnum -= 1
            # 从下到上
            if rnum >= 0 and len(out) < m * n:
                for j in range(rnum):
                    r -= 1
                    out.append(matrix[r][c])
                rnum -= 1
        return out

#
    # matrix类型为二维列表，需要返回列表
    def printMatrix2(self, matrix):
        out = []
        while matrix:
            # 上边界即为数组的第一个子数组。假设m*n矩阵，m,n分别为行数和列数
            # pop将矩阵看成看成m-1个元素，每个元素是个行向量
            out += matrix.pop(0)  # 第一行
            # 如果这里仅判断if matrix，那么对于测试数组例[[1],[2],[3]]，循环后变成了[[],[]]，matrix不为空
            if matrix and matrix[0]:
                # 右边界即为数组每一项的最后一个元素
                for row in matrix:
                    out.append(row.pop())
            # 下边界即为余下数组的最后一行
            if matrix:
                out += matrix.pop()[::-1]  # pop():最后一个行向量[::-1]逆序
            if matrix and matrix[0]:
                # 左边界即为数组从尾到头的每一项子数组的第一个元素
                # [::-1]将元素倒序，对于matrix而言，每个行向量是一个元素；pop(0)每个行向量的第一个元素
                for row in matrix[::-1]:
                    out.append(row.pop(0))
        return out


c = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]
#print(c.pop(2))#第3行输出
m,n=len(c),len(c[0])
print(c[::-1])#从下往上输出
print(len(c))
out=[]
for row in c[::-1]:
    print(row)
    out.append(row.pop(0))
print(out)

