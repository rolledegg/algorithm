'''
Floyd-Warshall Algorithm
시간 복잡도 : O(N^3)
'''

INF = int(1e9)
# 노드의 개수 및 간선의 개수를 입력 받기
n = int(input())
m = int(input())

# 2차원 그래프 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용을 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], (graph[a][k] + graph[k][b]))

# 수행된 결과를 출력
#if __name__ == "__main__":
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == INF:
                print("INFINITY", end=" ")
            else:
                print(graph[a][b], end=" ")
        print()


# Q1
import heapq

# 회사의 개수 N 경로의 개수 M
n, m = map (int, input().split())
# 그래프
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
# 방문 회사 X, 소개팅 K
x, k = map (int, input().split())

distance= [INF] * (n+1)
INF = int(1e9)
isvisited = False

def dijstra(start):
    q = []
    heapq.heappush(q,start)
    distance[start]=0
    while q:
        now = heapq.heappop(q)
        for i in graph[now]:
            cost = distance[now] +1
            if distance[i] > cost:
                distance[i] = cost
                heapq.heappush(q,i)

if __name__ == "__main__":
    way = 0

    dijstra(1)
    way += distance[k]
    dijstra(k)
    way += distance[x]

    if way > INF:
        print("-1")
    else:
        print(way)