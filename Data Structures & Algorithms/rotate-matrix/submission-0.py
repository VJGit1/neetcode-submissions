class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
    #Bec the matrix is always nXn so len(matrix)==len(matrix[0])
        #Transpose
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #Reverse rows
        for i in range(len(matrix)):
            matrix[i][:]=matrix[i][::-1]

        # for reversing, we could also use matrix[i].reverse()
        