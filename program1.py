class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code hereclass Solution:
        def dfs(i, j):
            # Check if the cell is out of bounds or water
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
                return
            # Mark the cell as water to avoid revisiting
            grid[i][j] = 'W'
            # Explore the neighboring cells (up, down, left, right)
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Count of islands
        island_count = 0

        # Traverse each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If the cell is land, it's a new island
                if grid[i][j] == 'L':
                    island_count += 1
                    dfs(i, j)  # Use DFS to mark all connected land cells

        return island_count

                    
        return 0
