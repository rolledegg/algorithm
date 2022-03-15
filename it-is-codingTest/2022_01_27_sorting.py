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
    # 시간 복잡도

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
