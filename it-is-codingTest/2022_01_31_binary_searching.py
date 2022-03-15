if __name__ == '__main__':
    '''
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def binary_search(arr, target, start, end):

        if(start>end):
            return

        middle = (start + end) // 2

        # target 중간점 비교
        if (arr[middle] == target):  # target이 중간갑이면 return
            return middle
        elif (arr[middle] < target):  # target이 더크면
            return binary_search(arr, target, middle + 1, end)  # 시작점을 middle+1 으로 옯기고 재귀
        else:  # target이 더 작으면
            return binary_search(arr, target, start, middle - 1)  # 끝 점을 middle-1로 옯기고 재귀

    print(binary_search(arr,5,0,10))
    '''

    # Q1
    '''
    n = int(input())
    stock_arr = list(map(int, input().split()))
    stock_arr.sort()

    m = int(input())
    item_arr = list(map(int, input().split()))


    def search_item(item, stock, start, end):

        mid = (start + end) // 2

        if (start == end):
            if stock[mid] != item:
                return False

        if stock[mid] == item:
            return True
        elif stock[mid] > item:
            return search_item(item, stock, start, mid - 1)
        else:
            return search_item(item, stock_arr, mid + 1, end)


    for i in item_arr:

        print(search_item(i, stock_arr, 0, n - 1), end=' ')
    '''

    # Q2
    n, m = map(int, input().split())
    dduck = list(map(int, input().split()))

    '''
    def cut_dduck(dduck, min, max):
        mid = (max + min) // 2

        dduck_sum = 0
        for i in dduck:
            if (i - mid > 0):
                dduck_sum += i - mid

        if (min == max):
            if dduck_sum != m:
                return mid

        if dduck_sum == m:
            return mid
        elif dduck_sum < m:
            return cut_dduck(dduck, min, mid)
        else:
            return cut_dduck(dduck, mid, max)


    print(cut_dduck(dduck, 0, max(dduck)))
    '''
    # 현재 얻을 수 있는 떡볶이의 양에 따라 자를 위치를 결정해야 하기 때문에 이를 재귀적으로 구현하는 것은 귀찮은 작업이 될 수 있다.
    # 파라메트릭 서치: 최적화 문제를 결정 문제('예' 혹은 '아니오'로 답라는 문제를 말한다)로 바꾸어 해결하는 기법이다.
    # 절단기 길이의 범위가 1~10억까지인데 이처럼 큰 수를 보면 당연하다는 듯이 가장 먼저 이진 탐색을 떠올려야 한다.
    start = 0
    end = max(dduck)
    height=0

    while (start <= end):

        mid = (start + end) // 2

        dduck_sum = 0
        for i in dduck:
            if (i > mid):
                dduck_sum += i - mid

        if dduck_sum < m:  # 절단기의 높이를 낮춰
            end = mid - 1
        else:  # 절단기의 놓이를 높여
            height = mid
            start = mid + 1

    print(height)
