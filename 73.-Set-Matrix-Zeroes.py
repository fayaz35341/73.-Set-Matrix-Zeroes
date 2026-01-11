class Solution:
    def setZeroes(self, matrix):
        row=set()
        col=set()
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        for i in row:
            matrix[i]=[0]*n
        for j in col:
            for i in range(m):
                matrix[i][j]=0
                
        # m=len(matrix)
        # n=len(matrix[0])
        # f_row=False
        # f_col=False

        # for j in range(n):
        #     if matrix[0][j]==0:
        #         f_row=True
        # for i in range(m):
        #     if matrix[i][0]==0:
        #         f_col=True
        # for i in range(1,m):
        #     for j in range(1,n):
        #         if matrix[i][j]==0:
        #             matrix[i][0]=0
        #             matrix[0][j]=0
        # for i in range(1,m):
        #     for j in range(1,n):
        #         if matrix[i][0]==0 or matrix[0][j]==0:
        #             matrix[i][j]=0
        # if f_row:
        #     for j in range(n):
        #         matrix[0][j]=0
        # if f_col:
        #     for i in range(m):
        #         matrix[i][0]=0

        # m=len(matrix)
        # n=len(matrix[0])
        # row=[0]*m
        # col=[0]*n
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j]==0:
        #              row[i]=1 
        #              col[j]=1
        # for i in range(m):
        #     for j in range(n):
        #         if row[i]==1 or col[j]==1:
        #             matrix[i][j]=0
#         return matrix

# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# print(Solution().setZeroes(matrix))
        
