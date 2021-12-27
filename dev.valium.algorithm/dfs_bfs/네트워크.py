def proc(computers, y, x):
    for i in range(len(computers[0])):
        if computers[x][i] == 1:
            computers[x][i] = 0
            proc(computers, x, i)

def solution(n, computers):
    output = 0
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] == 1:
                proc(computers, i, j)
                output += 1

    return output

if __name__ == '__main__':
    print(solution(5,  	[ [1, 1, 0],
                          [1, 1, 0],
                          [0, 0, 1]]))