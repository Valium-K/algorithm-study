output = 1
def proc(place, i, j, depth, visited):
    global output

    if depth >= 2 or output == 0:
        return

    # 상하좌우
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[i][j] = True

    for d in range(4):
        cur_i = i + direction[d][0]
        cur_j = j + direction[d][1]

        if cur_i < 0 or cur_i >= len(place) or 0 > cur_j or cur_j >= len(place[0]):
            continue

        cur = place[cur_i][cur_j]
        if not visited[cur_i][cur_j] and cur == "O":
            proc(place, cur_i, cur_j, depth + 1, visited)
        elif not visited[cur_i][cur_j] and cur == "X":
            continue
        elif not visited[cur_i][cur_j] and cur == "P":
            output = 0

def solution(places):
    global output
    answer = []

    for place in places:
        output = 1
        visited = [[False] * len(place[0]) for _ in place]
        for i in range(len(place)):
            for j in range(len(place)):
                if output == 1 and place[i][j] == "P":
                    proc(place, i, j, 0, visited)
        answer.append(output)

    return answer
if __name__ == '__main__':
    solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])