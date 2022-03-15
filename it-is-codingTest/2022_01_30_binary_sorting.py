if __name__ == '__main__':
    # 퀵 정렬
    # 시간 복잡도 O(NlogN)
    '''
    arr = [3, 5, 1, 8, 9, 0, 2, 4, 11, 0]

    def quick_sort(arr, start, end):
        if (start >= end):  # arr길이가 1이하이면 return
            return

        pivot = arr[start]
        left = start + 1
        right = end

        while (True):
            while (left <= end and arr[left] <= pivot):  # left가 <end 이고 현재값<=pivot
                left += 1

            # while (right >= start and arr[right] > pivot):
            # --> ERROR:  right>=start 이면 arr에 pivot보다 큰 값만 있을때 right=start-1까지 감 (right >= start+1)
            # arr[right] > pivot 이면 pivot과 같은 값이 arr에 들어가 있을 때 무한 루프
            while (right > start and arr[right] >= pivot):  # right가 >start & 현재값 >=pivot
                right -= 1

            if (left <= right):  # 안지나쳤으면 swqp
                arr[left], arr[right] = arr[right], arr[left]

            if (left > right):  # 지나쳤으면 pivot이랑 right swqp
                arr[start], arr[right] = arr[right], arr[start]
                break

        quick_sort(arr, start, right - 1)
        quick_sort(arr, right + 1, end)


    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
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