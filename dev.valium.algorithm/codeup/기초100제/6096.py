if __name__ == '__main__':
    d = [list(map(int, input().split())) for _ in range(19)]

    n = int(input())
    for _ in range(n):
        x, y = map(lambda num: num - 1, map(int, input().split()))

        for i in range(0, 19):
            if d[i][y] == 0:
                d[i][y] = 1
            else:
                d[i][y] = 0

            if d[x][i] == 0:
                d[x][i] = 1
            else:
                d[x][i] = 0

    for i in d:
        for j in i:
            print(j, end=' ')
        print()