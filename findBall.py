class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        width = len(grid[0])
        res = []
        for i in range(width):
            res.append(ballEnd(grid, i))
        return res

def ballEnd(grid, startColumn):
    height = len(grid)
    width = len(grid[0])
    currentColumn = startColumn
    currentRow = 0
    while currentRow < height:
        if grid[currentRow][currentColumn] == -1:
            if currentColumn - 1 < 0 or grid[currentRow][currentColumn - 1] != -1:
                return -1
            currentRow += 1
            currentColumn -= 1
        else:
            if currentColumn + 1 >= width or grid[currentRow][currentColumn + 1] != 1:
                return -1
            currentRow += 1
            currentColumn += 1
    return currentColumn