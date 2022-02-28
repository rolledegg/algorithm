if __name__ == '__main__':
    """
    Dynamic Programming
    예시) 피보나치 수열
    """


    # 단순 재귀함수
    def fibo(n):
        if n == 1 or n == 2:
            return 1
        return fibo(n - 1) + fibo(n - 2)


    # 다이나믹 프로그래밍
    # 방법1.
    # Topdown (메모이제이션)
    arr = [0] * 100


    def dyna_fibo(n):
        if n == 1 or n == 2:
            return 1
        if arr[n] != 0:
            return arr[n]
        arr[n] = dyna_fibo(n - 1) + dyna_fibo(n - 2)
        return arr[n]


    # print(dyna_fibo(40))

    # 방법1.
    # Bottomup
    arr2 = [0] * 100

    arr2[1] = 1
    arr2[2] = 1
    n = 40

    for i in range(3, n + 1):
        arr2[i] = arr2[i - 1] + arr2[i - 2]

    # print(arr2[40])

    # Q1

    # n = int(input())
    d = [0] * 30001

    for n in range(2, n + 1):

        d[n] = d[n - 1] + 1

        if (n % 2 == 0):
            d[n] = min(d[n], d[n // 2] + 1)

        if (n % 3 == 0):
            d[n] = min(d[n], d[n // 3] + 1)

        if (n % 5 == 0):
            d[n] = min(d[n], d[n // 5] + 1)

    # print(count[n])
    '''
    # Q2
    n = int(input())
    food = list(map(int, input().split()))
    select = False  # 전칸이 선택되어있는지 여부는 신경쓸 필요가 없구나...
    d = [0] * n

    d[0] = food[0]

    if food[0] >= food[1]:
        d[1] = food[0]
    else:
        select = True
        d[1] = food[1]

    for n in range(2, n):
        # 전칸이 선택되어있지 않다면 현재칸하고 전전칸까지의 값하고 합
        if select == False:
            d[n] = food[n] + d[n - 1]
            select = True
        # 전칸이 선택되어있다면 경우의 수 생각
        if d[n - 1] >= (food[n] + d[n - 2]):
            # 선택 안하고 넘김
            d[n] = d[n - 1]
        else:
            d[n] = food[n] + d[n - 2]
            select = True

    # print(d[n])
    '''
    # Q3
    n = int(input())
    d = [0] * 1001

    d[1] = 1
    d[2] = 3

    for i in range(3, n + 1):
        d[i] = d[i - 1] + (2 * d[i - 2])

    print(d[n] % 796796)


    # Q4
    n,m = map(int, input().split())
    coin = []
    for i in range(n):
        coin.append(int(input()))

    print(n,m,coin)


