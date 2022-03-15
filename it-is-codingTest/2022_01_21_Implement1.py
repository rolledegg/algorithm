<<<<<<< HEAD
# 시뮬레이션 유형 (일련의 명령에 다라서 개체를 차례대로 이동시킨다)
def traveling():
    n = int(input())
    # (y,x)
    x = 1
    y = 1  # -> x,y =1,1
    way = input().split()
    print(way)

    for distance in way:
        if (distance == "R"):
            if (x < n):
                x += 1
        elif (distance == "L"):
            if (x > 1):
                x -= 1
        elif (distance == "U"):
            if (y > 1):
                y -= 1
        elif (distance == "D"):
            if (y < n):
                y += 1

    print(y, x)

#def TravelingAnswer():



# 완전 탐색(가능한 경우의 수를 모두 검사해보는 탐색 방법)
def countThree():
    n = int(input())
    count = 0

    for h in range(n + 1):
        if h % 10 == 3:
            count += 60 * 60
            continue
        for m in range(60):
            if (m % 10 == 3) or (m // 10 == 3):
                count += 60
                continue
            for s in range(60):
                if (s % 10 == 3) or (s // 10 == 3):
                    count += 1

    print(count)


def AbleToMove():
    now = input()
    way = 0
    x = [0, "a", "b", "c", "d", "e", "f", "g", "h"]
    nowX, nowY = x.index(now[0]), int(now[1])

    if (nowX - 2 > 0 and nowY + 1 < 9):
        way += 1
    if (nowX - 2 > 0 and nowY - 1 > 0):
        way += 1
    if (nowX + 2 < 9 and nowY + 1 < 9):
        way += 1
    if (nowX + 2 < 9 and nowY - 1 > 0):
        way += 1

    if (nowY - 2 > 0 and nowX + 1 < 9):
        way += 1
    if (nowY - 2 > 0 and nowX - 1 > 0):
        way += 1
    if (nowY + 2 < 9 and nowX + 1 < 9):
        way += 1
    if (nowY + 2 < 9 and nowX - 1 > 0):
        way += 1

    print(way)


if __name__ == '__main__':
    # countThree()
    # traveling()
    AbleToMove()
=======
# 시뮬레이션 유형 (일련의 명령에 다라서 개체를 차례대로 이동시킨다)
def traveling():
    n = int(input())
    # (y,x)
    x = 1
    y = 1  # -> x,y =1,1
    way = input().split()
    print(way)

    for distance in way:
        if (distance == "R"):
            if (x < n):
                x += 1
        elif (distance == "L"):
            if (x > 1):
                x -= 1
        elif (distance == "U"):
            if (y > 1):
                y -= 1
        elif (distance == "D"):
            if (y < n):
                y += 1

    print(y, x)

#def TravelingAnswer():



# 완전 탐색(가능한 경우의 수를 모두 검사해보는 탐색 방법)
def countThree():
    n = int(input())
    count = 0

    for h in range(n + 1):
        if h % 10 == 3:
            count += 60 * 60
            continue
        for m in range(60):
            if (m % 10 == 3) or (m // 10 == 3):
                count += 60
                continue
            for s in range(60):
                if (s % 10 == 3) or (s // 10 == 3):
                    count += 1

    print(count)


def AbleToMove():
    now = input()
    way = 0
    x = [0, "a", "b", "c", "d", "e", "f", "g", "h"]
    nowX, nowY = x.index(now[0]), int(now[1])

    if (nowX - 2 > 0 and nowY + 1 < 9):
        way += 1
    if (nowX - 2 > 0 and nowY - 1 > 0):
        way += 1
    if (nowX + 2 < 9 and nowY + 1 < 9):
        way += 1
    if (nowX + 2 < 9 and nowY - 1 > 0):
        way += 1

    if (nowY - 2 > 0 and nowX + 1 < 9):
        way += 1
    if (nowY - 2 > 0 and nowX - 1 > 0):
        way += 1
    if (nowY + 2 < 9 and nowX + 1 < 9):
        way += 1
    if (nowY + 2 < 9 and nowX - 1 > 0):
        way += 1

    print(way)


if __name__ == '__main__':
    # countThree()
    # traveling()
    AbleToMove()
>>>>>>> 6aba3c3eafc2cf7db49c2cffe880295826b8855b
