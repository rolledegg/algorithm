if __name__ == '__main__':
    '''
    == 미로찾기 같은 시뮬레이션 문제 ==
       교재 p.119
    '''

    n, m = map(int, input().split())
    x, y, dir = map(int, input().split())
    # 방향 리스트
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 방문 여부 배열 초기화
    d = [[0] * m for _ in range(n)]
    d[x][y] = 1

    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))


    def turn_left():
        # 함수 안에서 전역변수를 사용할 수 있게 해주는 global keyword
        global dir
        dir -= 1
        if (dir == -1):
            dir = 3


    # 시뮬레이션
    count = 1
    turn_count = 0

    while (True):
        # turn left
        '''함수로 빼기
        dir -= 1
        if (dir == -1):
            dir = 3
        '''
        turn_left()
        turn_count += 1

        # 앞칸 구하기
        nx, ny = x + dx[dir], y + dy[dir]

        if (d[nx][ny] == 0 and array[nx][ny] == 0):  # 앞칸 방문x and 바다x
            x, y = nx, ny  # 한칸 앞으로
            d[x][y] = 1
            count += 1
            turn_count = 0
            continue

        if turn_count == 4:  # 사방에 직진할 곳 x
            # 뒷칸 구하기
            nx, ny = x - dx[dir], y - dy[dir]

            if array[nx][ny] == 0:  # 뒤가 육지면
                x, y = nx, ny  # 뒤로가
                turn_count = 0
            else:
                break;  # 게임 끝

    print(count)
