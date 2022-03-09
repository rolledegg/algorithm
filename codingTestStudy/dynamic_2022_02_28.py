#Q4
n,m = map(int,input().split())

coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort()

d = [0] * (m+1)
# 초기값 초기화
# 가장 큰 코인을 뺸 값이 양수면 +1, 모든 코인 종료 뺀 값이 -1 이면 -1
for i in range(1,m+1):
    for j in range(n-1,-1,-1):
        if i - coin[j] < 0:
            continue

        if d[i - coin[j]] >= 0:
            d[i] = d[i - coin[j]] + 1
            break

    if d[i] == 0:
        d[i] = -1

if __name__ == '__main__':
    print(d[m])
