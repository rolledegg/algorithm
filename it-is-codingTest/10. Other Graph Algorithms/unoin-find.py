# 특정 원소가 속한 집합을 찾기
'''
비효율 적인 find function
함수의 시간 복잡도 O(v)
'''
def find_set(parent, a):
    #if parent[a] == a:
    #    return a
    #else:
    #    return find_set(parent,parent[a])
    if parent[a] != a:
        return find_set(parent,parent[a])
    return a

''' 
효율적인 find function
parent값을 find하면서 갱신시켜서  
힘수의 시간 복잡도가 줄어든다.
'''
def find_set2(parent, a):
    if parent[a] != a:
        parent[a] = find_set2(parent, parent[a])
    return parent[a]


# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a= find_set(parent,a)
    b= find_set(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


# 노드 개수, 간선 개수(연산 개수)
v,e = map(int,input().split())
# 부모 테이블 초기화
p=[0] * (v+1)
for i in range(1,v+1):
    p[i] = i
# union 연산
for _ in range(e):
    a,b = map(int,input().split())
    union_parent(p,a,b)

if __name__=="__main__":
    # 각 원소가 속한 집합 출력
    print("각 원소가 속한 집합: ", end="")
    for i in range(1,v+1):
        print(find_set2(p, i), end=" ")

    print()

    # 부모 테이블 내용 출력
    print("부모 테이블: ", end="")
    for i in range(1,v+1):
        print(p[i], end=" ")



