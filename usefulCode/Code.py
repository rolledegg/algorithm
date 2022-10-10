'''
== 알파벳 순서를 정수 순서로 바꾸는 방법 ==
'''
alpabet = ['a', 'b', 'c', 'd', 'e', 'f']
for i in alpabet:
    # ord(): 문자의 아스키 코드값을 리턴하는 함수
    aToInt = ord(i) - ord('a') + 1
    print(aToInt)

'''
== [N][M]크기의 리스트 초기화 => list Comprehension
'''
M, N = 5, 5
array = [[0] * M for _ in range(N)]

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
    nextX = nowX + steps[i][0]
    nextY = nowY + steps[i][1]
    # 공간 벗어나면 무시 / 카운트 x
    if (nextX < 1 or nextY < 1 or nextX > 8 or nextY > 8):
        continue
    # 이동
    nowX, nowY = nextX, nextY

'''
== [[]]*n VS [[] for _ in n] 
'''
list1=[[] for _ in range(5)]    # [[], [], [], [], []]
list2=[[]] * 5                  # [[], [], [], [], []]
list3=[[] * 5]                  # [[]]
list4=[[0] * 5]                 # [[0, 0, 0, 0, 0]]
list5=[0] * 5                   # [0, 0, 0, 0, 0]

list1[0].append(1)  # [[1], [], [], [], []]
list2[0].append(1)  # [[1], [1], [1], [1], [1]]
list4[0][0] = 1     # [[1, 0, 0, 0, 0]]
list5[0] = 1     # [1, 0, 0, 0, 0]
'''=== list1과 list5만 사용 ==='''

'''
== 리스트롸 튜플을 원소로 가지고 있는 리스트 정렬
== 원소의 첫번째 인덱스 기준 오름차순 정
'''
a=[[5,3],[1,4],[9,0]]
b=[(15,3),(1,14),(9,10)]
a.sort()    # [[1, 4], [5, 3], [9, 0]]
b.sort()    # [(1, 14), (9, 10), (15, 3)]

# 특정문자열에서 특정 문자들 제거
for i in new_id:
	if (i not in "~!@#$%^&*()=+[{]}:?,<>/"):
		answer += i
