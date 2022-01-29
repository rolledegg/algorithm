if __name__ == '__main__':

    # 선택 정렬
    # 시간 복잡도 O(N^2)
    ''' 
    arr = [3, 5, 1, 8, 9, 0, 2, 4]

    for i in range(len(arr)):
        # 작은 값의 인덱스
        min_index = i
        for j in range(i, len(arr)):
            if (arr[j] <= arr[min_index]):
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]

    print(arr)
    '''

    # 삽입 정렬
    # 시간 복잡도 O(N^2)
    '''
    arr = [3, 5, 1, 8, 9, 0, 2, 4]
    for i in range(1, len(arr)):  # 1 ~ 7
        for j in range(i, 0, -1):  # i-1 ~ 0
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    print(arr)
    '''

    # 퀵 정렬
    # 시간 복잡도 O(NlogN)
    '''
    arr = [3, 5, 1, 8, 9, 0, 2, 4]

    def quick_sort(arr, start, end):
        if (start >= end):
            return

        pivot = start
        left = start + 1
        right = end

        while (left <= right):
            while left <= end and arr[left] <= arr[pivot]:
                # while left < end and arr[left] <= arr[pivot]: Error
                left += 1
            while right > start and arr[right] >= arr[pivot]:
                # while right > start +1  and arr[right] >= arr[pivot]: Error
                right -= 1

            if (left > right):
                arr[pivot], arr[right] = arr[right], arr[pivot]
            else:
                arr[left], arr[right] = arr[right], arr[left]

        quick_sort(arr, start, right - 1)
        quick_sort(arr, right + 1, end)


    def quick_sort2(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        tail = arr[1:]

        left = [x for x in tail if x < pivot]
        right = [x for x in tail if x >= pivot]

        return quick_sort2(left) + [pivot] + quick_sort2(right)


    # quick_sort(arr, 0, len(arr) - 1)
    print(quick_sort2(arr))
    '''

    # 계수 정렬
    # O(N+K)
    # 책에서는 mim을 당연히 0으로 생각하고 있음 (아마 범위가 거의 정수이기 때문?)
    # 나는 mim이 0이 아닌경우를 고려해서 작성했음
    '''
    arr = [7, 5, 9, 3, 3, 1, 6, 2, 11, 1, 4, 8, 7, 5, 2]
    min_value = min(arr)
    max_value = max(arr)

    range_arr = [0 for _ in range(max_value - min_value + 1)]

    for i in arr:
        range_arr[i - min_value] += 1

    sorted_list = []
    for i in range(len(range_arr)):
        for j in range(range_arr[i]):
            sorted_list.append(i + min_value)

    print(sorted_list)
    '''
    # Q1
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))

    arr.sort()
    arr.reverse()
    for i in arr:
        print(i, end=' ')

    # 2
    n = int(input())
    arr = []
    for i in range(n):
        name, score = map(str, input().split())
        arr.append((name, int(score)))


    def setting(data):
        return data[1]


    sorted_list = sorted(arr, key=setting)
    for i in range(len(sorted_list)):
        print(sorted_list[i][0], end=' ')

    # Q3
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(k):
        a_min = a.index(min(a))  # find A's min index
        b_max = b.index(max(b))  # find B's maz index
        if(a[a_min]<b[b_max]):
            a[a_min], b[b_max] = b[b_max], a[a_min] #swip

    print(sum(a))