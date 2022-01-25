if __name__ == '__main__':
    n, m = map(int, input().split())
    ice = []
    for i in range(n):
        ice.append(list(map(int, input().split())))

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    visited = [[False] * m for _ in n]

    count = 0


    def dfs(ice, start, visited):
        x, y = start
        visited[x][y] = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx, 0 or ny < 0 or nx > n - 1 or ny > m - 1):
                continue
            if ice[nx][ny] == 0 and not visited[nx][ny]:
                x, y = nx, any(dfs(ice, (x, y), visited))


    for x in range(n):
        for y in range(m):
            if ice[x][y] == 0 and not visited[x][y]:
                count += 1
                dfs(ice, (x, y), visited)

    print(count)