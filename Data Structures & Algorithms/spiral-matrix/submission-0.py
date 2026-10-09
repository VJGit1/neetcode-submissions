class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        top=0
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        left=0
        while top<=bottom and left<=right:
            #traversing top row
            #Top row →→→
            for j in range(left,right+1):
                res.append(matrix[top][j])
            top+=1
            #traverse right column
            # Right column ↓↓↓
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1
           
            #traversing bottom row backwards
            # Bottom row ←←←
            if top<=bottom:
                for j in range(right,left-1,-1):
                    res.append(matrix[bottom][j])
                bottom-=1
              
            # Left column ↑↑↑
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
        return res