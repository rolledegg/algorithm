
'''
== 알파벳 순서를 정수 순서로 바꾸는 방법 ==
'''
alpabet = ['a', 'b', 'c', 'd', 'e', 'f']
for i in alpabet:
    # ord(): 문자의 아스키 코드값을 리턴하는 함수
    aToInt = ord(i) - ord('a') + 1
    print(aToInt)

''' 
== 시뮬레이션 유형 (일련의 명령에 따라서 개체를 차례대로 이동시킨다) ==
'''
# 1.현재 위치 입력받기
nowX, nowY = 1, 1

# 2.이동할 수 있는 방향
# ex1) x,y 따로 (L,R,U,D 입력 받음. 공간 벗어나면 무시)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', "D"]
# ex2) x,y 같이 (현재 위치에서 8가지 step중 몇 가지 step이 공간에서 벗어나지 않고 가능한지 측정)
steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

# 3.이동 후의 좌표 구하기
for i in range(len(steps)):
    nextX = nowX+ steps[i][0]
    nextY = nowY + steps[i][1]
    # 공간 벗어나면 무시 / 카운트 x
    if(nextX<1 or nextY<1 or nextX>8 or nextY>8):
        continue
    # 이동
    nowX, nowY = nextX, nextY

