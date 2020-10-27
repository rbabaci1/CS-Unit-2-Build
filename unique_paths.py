"""
Plan:
Do DFS to get to the goal node
Backtrack if:
1. the current cell we're visiting is invalid (-1)
2. if we're out of bounds
3. if we're at the goal node (2) and we haven't visited each cell yet

Mark each visited cell as -1 so that we don't visit it again

We know all the valid cells are visited if all the cells in the maze don't
have a 0 cell


"""
class Solution:
    res = 0 # num unique ways to get from start to end
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        startingPoint = self.findStartingPoint(grid)
        if startingPoint == None:
            return 0
        self.uniquePathsHelper(grid, startingPoint[0], startingPoint[1])
        return self.res
    
    def uniquePathsHelper(self, grid, x, y):
        width, height = len(grid[0]), len(grid)
        # backtrack if out of bounds or if -1 cell
        if x < 0 or y < 0 or x >= width or y >= height or grid[y][x] == -1:
            return
        # if we're at goal cell, then check if all valid cells have been visited
        if grid[y][x] == 2:
            for i in range(height):
                for j in range(width):
                    if grid[i][j] == 0:
                        return
            # we've visited all valid cells, so this is a valid solution
            self.res += 1
            return
        # when we visit a 0, or 1 cell, mark it as visited
        grid[y][x] = -1
        # visit neighbors
        self.uniquePathsHelper(grid, x + 1, y)
        self.uniquePathsHelper(grid, x - 1, y)
        self.uniquePathsHelper(grid, x, y + 1)
        self.uniquePathsHelper(grid, x, y - 1)
        grid[y][x] = 0
            
    
    def findStartingPoint(self, grid):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    return (x, y)
        return None
