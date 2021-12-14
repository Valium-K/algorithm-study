def solution(rows, columns, queries):
    answer = []

    mat = [[] for _ in range(rows)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            mat[i-1].append((i-1)*columns + j)

    for query in queries:
        stack = []
        dir_query = [
            (query[0]-1, query[1]-1),
            (query[0]-1, query[3]-1),
            (query[2]-1, query[3]-1),
            (query[2]-1, query[1]-1)
        ]
        staring_point = dir_query[0]
        temp = 0
        prev = 0

        while dir_query[0] != dir_query[1]:
            temp = mat[dir_query[0][0]][dir_query[0][1]]
            mat[dir_query[0][0]][dir_query[0][1]] = prev
            prev = temp
            dir_query[0] = (dir_query[0][0], dir_query[0][1] + 1)
            stack.append(prev)

        while dir_query[1] != dir_query[2]:
            temp = mat[dir_query[1][0]][dir_query[1][1]]
            mat[dir_query[1][0]][dir_query[1][1]] = prev
            prev = temp
            dir_query[1] = (dir_query[1][0] + 1, dir_query[1][1])
            stack.append(prev)

        while dir_query[2] != dir_query[3]:
            temp = mat[dir_query[2][0]][dir_query[2][1]]
            mat[dir_query[2][0]][dir_query[2][1]] = prev
            prev = temp
            dir_query[2] = (dir_query[2][0], dir_query[2][1] - 1)
            stack.append(prev)

        while dir_query[3] != staring_point:
            temp = mat[dir_query[3][0]][dir_query[3][1]]
            mat[dir_query[3][0]][dir_query[3][1]] = prev
            prev = temp
            dir_query[3] = (dir_query[3][0] - 1, dir_query[3][1])
            stack.append(prev)
        mat[staring_point[0]][staring_point[1]] = prev

        answer.append(min(stack))

    return answer

if __name__ == '__main__':
    print(solution(4,3,[[1,1,2,3]]))