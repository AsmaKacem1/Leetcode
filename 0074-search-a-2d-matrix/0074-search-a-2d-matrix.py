class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix[0])
        m=len(matrix)
        for i in range (m):
            if(matrix[i][n-1])>=target:
                for j in range(n):
                    if (matrix[i][j]==target):
                        return True
                return False
        