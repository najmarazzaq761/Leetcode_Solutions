class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
           #.................. dfs ........................
        # start_color = image[sr][sc]
        # if image[sr][sc] == color:
        #     return image
        # def dfs(r,c):
        #     if r<0  or r>=rows or c<0 or c>=cols:
        #         return
        #     if image[r][c] != start_color:
        #         return 
        #     image[r][c] = color

        #     dfs(r-1,c)
        #     dfs(r+1,c)
        #     dfs(r,c-1)
        #     dfs(r,c+1)
        # dfs(sr, sc)
           # .................... bfs .......................
        stack = [(sr,sc)]
        original_color = image[sr][sc]
        if original_color == color:
            return image
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while stack:
            x, y = stack.pop()
            image[x][y] = color
            for dx,dy in directions:
                nx,ny = x+dx, y+dy
                if 0<=nx <rows and 0<=ny <cols and image[nx][ny] == original_color:
                    stack.append((nx, ny))
        return image 