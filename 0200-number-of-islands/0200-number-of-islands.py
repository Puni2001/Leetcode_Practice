class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            # Base case: Out of bounds or water cell
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            # Mark the cell as visited
            grid[r][c] = '0'

            # Explore all 4 possible directions (up, down, left, right)
            dfs(r+1, c)  # Down
            dfs(r-1, c)  # Up
            dfs(r, c+1)  # Right
            dfs(r, c-1)  # Left

        # Iterate over every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # If it's land, start DFS
                    island_count += 1
                    dfs(r, c)  # Mark the entire island as visited

        return island_count