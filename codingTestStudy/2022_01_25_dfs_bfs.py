if __name__ == '__main__':
    n, m = map(int, input().split())
    ice = []
    for i in range(n):
        ice.append(list(map(int, input())))

    '''
    == 내 풀이 (거의 비슷) ==
    dx = [0, 1, 0, -1] # 동 남 서 북
    dy = [1, 0, -1, 0]

    visited = [[False] * m for _ in range(n)]
   
    count = 0


    def dfs(ice, start, visited):
        x, y = start
        visited[x][y] = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx< 0 or ny < 0 or nx > n - 1 or ny > m - 1):
                continue
            if ice[nx][ny] == 0 and not visited[nx][ny]:
                dfs(ice, (nx, ny), visited)


    for x in range(n):
        for y in range(m):
            if ice[x][y] == 0 and not visited[x][y]:
                count += 1
                dfs(ice, (x, y), visited)
    '''


    def dfs(x, y):
        if (x < 0 or y < 0 or x >= n or y >= m):
            return False

        if ice[x][y] == 0:
            ice[x][y] = 1

            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)
            return True
        return False


    count = 0
    for x in range(n):
        for y in range(m):
            if dfs(x, y):
                count += 1

    print(count)
