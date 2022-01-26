from collections import deque

if __name__ == '__main__':
    n, m = map(int, input().split())

    maze = []
    for i in range(n):
        maze.append(list(map(int, input())))

    count = [[1] * m for _ in range(n)]

    dx = [0, 1, 0, -1]  # 동 남 서 북
    dy = [1, 0, -1, 0]

    start = (0, 0)
    result = 1
    queue= deque()
    #queue = deque([start])  # 시작 좌표 큐에 넣기
    #queue = deque(start)  >> TypeError:  cannot unpack non-iterable int object
    queue.append(start)
    maze[start[0]][start[1]] = 0  # 시작점 방문처리 ->0처리

    while (queue):  # 큐 빌 때까지 반복
        x, y= queue.popleft()  # 큐 pop
        for i in range(4):  # 인접 노드 중 방문 안한 노드 큐에 넣기    상단 값+1 삽입
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1):
                continue

            if maze[nx][ny] == 1:
                count[nx][ny] = count[x][y] + 1
                queue.append((nx, ny))
                maze[nx][ny]=0

    print(count[n-1][m-1])
