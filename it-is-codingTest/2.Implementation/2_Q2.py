# 게임 개발
'''
캐릭터가 있는 장소는 1 * 1 크기의 정사각형으로 이뤄진 N * M  크기의 정사각형으로, 각각의 칸은 육지 또는 바다이다.
캐릭터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은 (A, B)로 나타낼 수 있고, A는 복쪽으로붜 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.
캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 었다. 캐릭터의 움직임을 설정하기 위해 정해 놓은 메뉴얼은 이러하다.
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 외쪽방향으로 회전한 다음 왼쪽으로 한 칸 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
    단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
위 과정을 반복적으로 수행하면서 캐린터의 움직임에 이상이 있는제 테스트하려고 한다. 메쥬얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.
[입력 조건]
- 첫 째 줄에 맵의 세로크기 N과 가로크기 M을 공백으로 구분하여 입력한다. (3<=N,M<=50)
- 둘 째 줄에 게임 캐릭터가 있는 칸의 좌표 (A,B)와 바라보는 방향을 각각 서로 공백으로 구분하여 주어진다. (0:북,1:동,2:남,3:서)
- 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다.
    맵의 외곽은 항상 바다로 되어있다.(0:육지, 1:바다)
- 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.
[출력 조건]
- 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
'''
n, m = map(int, input().split())
x, y, d = map(int, input().split())

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

game_board = [[] for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for i in range(n):
    input_data = list(map(int, input().split()))
    game_board[i].extend(input_data)

count = 1
visited[x][y] = 1
turn_time = 0
isFinish = False


def turn_left():
    global d
    d -= 1
    if(d == -1):
        d = 3


while True:
    turn_left()
    
    nx= x + dx[d]
    ny= y + dy[d]

    if game_board[nx][ny] == 0 and visited[nx][ny] == 0:# 왼쪽 칸이 가보지 않은 육지 라면
            x, y = nx, ny
            visited[x][y] = 1
            count += 1
            turn_time = 0
    else:
        turn_time += 1

    if(turn_time == 4 ):
        nx = x - dx[d]
        ny = y - dy[d]

        if game_board[nx][ny] == 0:
            x,y = nx,y
            turn_time = 0
        else:
            break


print(count)
'''
while not isFinish:
    while turn < 4:
        # 회전
        if d == 0:
            d= 3
        else:
            d = d - 1

        nx = x + dx[d]
        ny = y + dy[d]

        if game_board[nx][ny] == 0 and visited[nx][ny] == 0:# 왼쪽 칸이 가보지 않은 육지 라면
            x, y = nx, ny
            visited[x][y] = 1
            count += 1
            turn = 0
        else:  # 아니라면
            turn += 1

    # 네면이 전부 아니라면
    # 뒤쪽방향이 바다인지 확인
    nx = x - dx[d]
    ny = y - dy[d]

    if game_board[nx][ny] == 1: # 맞다면 종료
        isFinish = True
    else:
        x,y = nx, ny
        turn = 0
print(count)
'''