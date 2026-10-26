class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        path=set()
        def dfs(r,c,i):
            #base case:if i reaches the length of word (meaning we matched every character)
            if i==len(word):
                return True
            #base case:out of bounds or we 
            #already visited it the current path
            if(r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[i] or (r,c) in path):
                return False
            #mark current cell as visited
            path.add((r,c))
            #explaoring up,down,left,right directions for next letter i+1
            #Check all 4 directions; save result so we can clean up the path before returning
            found = (
            dfs(r + 1, c, i + 1)  # Down
            or dfs(r - 1, c, i + 1)  # Up
            or dfs(r, c + 1, i + 1)  # Right
            or dfs(r, c - 1, i + 1))  # Left
        #Remove the cell from path so other starting paths can use it
            path.remove((r,c))
            return found
        #scan every cell in grid to find valid starting letter word[0]
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False