class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """

        better solution

        m = len(matrix)
        n = len(matrix[0])

        rows = [False] * m 
        cols = [False] * n 

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

        """

        n = len(matrix)
        m = len(matrix[0])

        cell0 = 1

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0

                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        cell0 = 0

        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] != 0:
                     # check for row or col if it is 0
                     if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

        # nOW Hanfle first row
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        
        # now handle first col
        if cell0 == 0:
            for i in range(n):
                matrix[i][0] = 0
