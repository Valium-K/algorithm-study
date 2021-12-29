from collections import deque

def solution(maps):
    ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = deque([(0, 0, -1)])

    while stack:
        y, x, step = stack.popleft()

        for d in ds:
            if 0 <= y + d[0] < len(maps) and 0 <= x + d[1] < len(maps[0]) and maps[y + d[0]][x + d[1]] == 1:
                maps[y + d[0]][x + d[1]] = step - 1
                stack.append((y + d[0], x + d[1], step - 1))

    return -1 if maps[len(maps) - 1][len(maps[0]) - 1] == 1 else -maps[len(maps) - 1][len(maps[0]) - 1]


if __name__ == '__main__':
    print(solution([
        [1,1,1],
        [1, 1, 1],
        [1, 1, 1]
    ]))

    print(2^5)