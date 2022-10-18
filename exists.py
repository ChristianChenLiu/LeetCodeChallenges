class Solution(object):
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        def backtrack(ri, cj, curr):
            if curr >= len(word): return True
            
            for i, j in directions:
                nr, nc = ri + i, cj + j
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == word[curr]:
                    board[nr][nc] = '#'
                    if backtrack(nr, nc, curr + 1): return True
                    board[nr][nc] = word[curr]
            return False
        
        for i in range(m):
             for j in range(n):
                    if board[i][j] == word[0]:
                        board[i][j] = '#'
                        if backtrack(i, j, 1): return True
                        board[i][j] = word[0]
        return False