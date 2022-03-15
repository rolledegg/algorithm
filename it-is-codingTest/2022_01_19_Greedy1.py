import time


def cardGame():
    n, m = map(int, input().split())
    data = []
    bigestOfSmall = 0;
    for i in range(0, n):
        data.append(list(map(int, input().split())))
        # if(bigestOfSmall < min(data[i])):
        #    bigestOfSmall = min(data[i])
        bigestOfSmall = max(bigestOfSmall, min(data[i]))

    print(bigestOfSmall)


def untilOne():
    n, k = map(int, input().split())
    count = 0;
    start = time.time()
    while (n != 1):
        if (n % k == 0):
            n = n / k
            count += 1
        else:
            n -= 1
            count += 1

    finish = time.time()
    print(count, finish - start)


def bigUntilOne():
    n, k = map(int, input().split())
    count = 0;
    start = time.time()

    while (n >= k):
        if (n % k == 0):
            n = n / k
            count += 1
        else:
            n -= (n % k)
            count += (n % k)

   # count+= n-1
    finish = time.time()

    print(count, finish - start)

if __name__ == '__main__':
    # cardGame()
    # untilOne()
    bigUntilOne()
