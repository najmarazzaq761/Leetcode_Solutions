class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh+=1
        mins = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            r,c,mins = queue.popleft()
            for dr, dc in directions:
                nr,nc = r+dr , c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh-=1
                    queue.append((nr,nc,mins+1))
        return mins if fresh==0 else -1
        