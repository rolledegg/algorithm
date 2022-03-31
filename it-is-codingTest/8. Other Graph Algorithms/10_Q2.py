# === Q2. 도시 분할 계획 === #
"""
마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다. 길은 어느 방향으로든지 다닐 수 있는 길이다.
그리고 길마다 길을 유지하는데 드는 유지비가 있다.
이장은 마을을 2개의 분리된 마을로 분할할 계획을 세우고 있다. 마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다.
각 분리된 마을 안에 있는 임의의 두집 사이에 경로가 항상 존재해야 한다는 뜻이다 마을에는 집이 하나 이상 있어야 한다.
일단 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다.
마을의 이장은 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다.
이것을 구하는 프로그램을 작성하시오.

[입력조건]
- 첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. N은 2 이상 100,000이하인 정수이고, M은 1 이상 1,000,000 이하인 정수이다.
- 그다음 줄부터 M줄에 걸쳐 길의 정보가 A,B,C 3개의 정수로 공백으로 구분된 어지는데 A번 집과 B번 집을 연결하는 길의 유지비가 C라는 뜻이다.
[출력조건]
- 첫쨰 줄에 길을 없애고 남은 유지비 합의 초솟값을 출력한다.
"""

n,m = map(int, input().split())
p = [0] * (n+1)
for i in range(1,n+1):
    p[i]=i

def find_parent(parent,x):
    if(parent[x] != x):
        parent[x]= find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if( a > b):
        parent[a] = b
    else:
        parent[b] = a

edges = []
result = 0
last = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))

edges.sort()

'''
민지 버전
for edge in edges:
    a = find_parent(p,edge[1])
    b = find_parent(p,edge[2])
    if(a==b):
        continue
    else:
        union_parent(p, edge[1], edge[2])
        result +=edge[0]
        last = result
'''

for edge in edges:
    cost,a,b = edge
    if(find_parent(p,a)==find_parent(p,b)):
        continue
    else:
        union_parent(p, a, b)
        result += cost
        last = cost

print(result - last)

# 해답 = 최소신장트리를 찾은뒤 가장 큰 비용의 간선 하나를 제거
