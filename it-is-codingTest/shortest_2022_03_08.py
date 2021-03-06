import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 변호 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

'''
1.간단한 다익스트라 알고리즘
  시간 복잡도: O(N^2)
'''
# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def easy_dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start]=0
    visited[start]= True
    for j in graph[start]:
        distance[j[0]] = j[1] # 인접한 노드의 최단 거리 초기화
    # 시작 노드를 제외한 전체 n -1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결되 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] +j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
'''
2.개선된 다익스트라 알고리즘
  시간복잡도: O(ElogV)
  E:노드 수 V:간선 수 Heap에 원소 삽입/삭제 시간:O(logN)
  한 번 처리된 노드는 더 이상 처리되지 않는다. -> while문은 V 이상 반복 X
  V번 반복될 때마다 각각 자신과 연결된 간선들을 모두 확인
  -> 현재 우선 순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총횟수 = 회대 간선의 개수

  따라서. 다익스트라 최단 경로 알고리즘은 E개의 원소를 우선순위 큐에 넣었다가 모두 뺴내는 연산과 유사
  -> O(2ElogE) -> O(ElogE) > O(ElogV^2) ->O(ElogV) 
'''
def fast_dijkstra(start):
    # visited 안만듬 pop 된게 방문했다는 의미가 됌
    q = [] # 힙 생성
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q: # 힙이 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처러된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(cost, i[0])

if __name__ == '__main__':
    easy_dijkstra(start)
    for i in range(1, n+1):
        # 도달할 수 없는 경우 INF라고 출력
        if distance[i] == INF:
            print("INFINITY")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(distance[i])
