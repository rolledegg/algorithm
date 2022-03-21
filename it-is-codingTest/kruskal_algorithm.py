def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
p = [0] * (v + 1)
for i in range(1, v + 1):
    p[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
# 간선을 비용순으로 정렬
edges.sort()

for i in range(e):
    cost, a, b = edges[i]
    if find_parent(p, a) == find_parent(p, b):
        continue
    union_parent(p, a, b)
    result += cost

if __name__ == "__main__":
    print(result)
