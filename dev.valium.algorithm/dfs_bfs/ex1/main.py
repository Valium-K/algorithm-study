def ice_cream(graph, row, col):
    graph[row][col] = 2

    # 상
    if row - 1 >= 0 and graph[row-1][col] == 0:
        ice_cream(graph, row - 1, col)
    # 하
    if row + 1 <= len(graph) - 1 and graph[row+1][col] == 0:
        ice_cream(graph, row + 1, col)
    # 좌
    if col - 1 >= 0 and graph[row][col-1] == 0:
        ice_cream(graph, row, col - 1)
    # 우
    if col + 1 <= len(graph[0]) - 1 and graph[row][col+1] == 0:
        ice_cream(graph, row, col + 1)

if __name__ == '__main__':

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for i in range(n):
        row = input()

        for j in range(len(row)):
            graph[i].append(int(row[j]))

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
                ice_cream(graph, i, j)

    print(count)