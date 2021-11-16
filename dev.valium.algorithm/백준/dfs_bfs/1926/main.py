from collections import deque

def get_largest_area(paint_map, y, x, depth):
    # 상 하 좌 우
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque([(y, x)])
    while q:
        target_y, target_x = q.popleft()

        for i in range(len(dir)):
            next_y, next_x = target_y + dir[i][0], target_x + dir[i][1]

            if 0 <= next_y < len(paint_map) and 0 <= next_x < len(paint_map[0]):
                if paint_map[next_y][next_x] == 1:
                    paint_map[next_y][next_x] = 9
                    depth += 1
                    q.append((next_y, next_x))

    if depth <= 1:
        return depth
    else:
        return depth-1

if __name__ == '__main__':
    n, m = map(int, input().split())
    paint_map = [ list(map(int, input().split())) for _ in range(n) ]

    output_arr = []
    for i in range(n):
        for j in range(m):
            if paint_map[i][j] == 1:
                output_arr.append(get_largest_area(paint_map, i, j, 1))


    if output_arr:
        print(len(output_arr))
        print(max(output_arr))
    else:
        print(len(output_arr))
        print(0)
