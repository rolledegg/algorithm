# === Q3. 커리큘럼 ===#
'''
동빈이는 온라인으로 강의 를 듣고 있다. 선수강의가 있는 강의는 선수 강의를 먼저 들어야만 해당 강의를 들을 수 있다.
동빈이는 총 N개의 강의를 듣고자 한다. 모든 강의는 1번부터 N번까지의 번호를 가진다.
또한 동시에 여러 개이 강의르르 들을 수 있다고 가정한다. 예를 들어 N=3일 때, 3번 강의의 선수 강의로 1번과 ㅈ번 강의가 있고,
1번과 2번 강의는 선수 강의가 없다고 가정하자. 그리고 각 강의에 대하여 강의 시간이 다음과 같다고 가정하자.
-1번: 30시간
-2번: 20시간
-3번: 40시간
이 경우 1번 강의를 수강하기까지의 최소 시간은 30시간, 2번 강의를 수강하기까지의 최소시간은 20시간 3번강의를 수강하기까지의 최소 시간은 70시간이다.

동빈이가 듣고자 하는 N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하는 프로그램을 작성하시오.

[입력 조건]
- 첫 쨰 줄에 동빈이가 듣고자 하는 강의의 수N(1 <= N <= 500) 이 주어진다.
- 다음 N개의 줄에는 각 강의의 시간과 그 강의를 듣기 위해 먼저 들어야하는 강의들의 번호가 자연수로 주어지며, 각 자연수는 공백으로 구분된다.
  이때 강의 시간은 100,000 이하의 자연수이다.
- 각 강의 번호는 1부터 N까지로 구성되며 각 줄은 -1로 끝난다.
[출력 조건]
- N개의 강의에 대하여 수강하기까지 최소 시간을 한 줄에 하나씩 출력한다.
'''

from collections import deque

# n = int(input())
v = int(input())
# edges=[[] for _ in range(n+1)]
graph = [[] for _ in range(v + 1)]
indegree = [0] * (v + 1)
min = [0] * (v + 1)
hours = [0] * (v + 1)
q = deque()

for i in range(1, v + 1):
    val = map(int, input().split())

    hours[i] = val[0]
    for x in val[1:-1]:
        graph[x].append(i)  # j->i
        indegree[i] += 1
'''
    for j in val:
        if hours[i] == 0:
            hours[i] = j
            continue
        if j != -1:
            graph[j].append(i)  # j->i
            indegree[i] += 1
'''

for i in range(1, v + 1):
    if indegree[i] == 0:
        q.append(i)
        min[i] = hours[i]

while q:
    now = q.popleft()
    for i in graph[now]:  # 연결 간선 확인
        indegree[i] -= 1  # 진입 차수 -1씩
        min[i] = max(min[i], min[now])  # min_pre 업데이트 max로

        if indegree[i] == 0:  # 진입차수가 0이면 큐에 넣기 min_pre
            q.append(i)
            min[i] += hours[i]

for i in range(1, v + 1):
    print(min[i])
