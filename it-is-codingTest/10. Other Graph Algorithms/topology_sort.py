from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v,e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(e):
    a,b = map(int, input().split())
    graph[a].append(b) # a->b 방향 그래프
    indegree[b]+=1 # 진입 차수 1증가

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()
    # 진입 차수가 0인 노드 전부 큐에 넣기
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
            #break(x) // 처음에 진입차수 0인 노드 전부 넣기

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i]-=1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=" ")

topology_sort()