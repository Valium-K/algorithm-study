if __name__ == '__main__':
    h, w = map(int, input().split())

    arr = [[0] * w for i in range(h)]

    for _ in range(int(input())):
        l, d, y, x = map(int, input().split())
        x -= 1
        y -= 1
        for i in range(l):
            try:
                arr[y][x] = 1
                if d == 0:
                    x += 1
                else:
                    y += 1
            except:
                continue

    for i in arr:
        for j in i:
            print(j, end=' ')
        print()