from collections import deque

def solve_maze(maze_map, target_y, target_x):
    queue = deque()
    queue.append((0, 0, 1))
    out = 123456789
    maze_map[0][0] = 0

    while queue:
        y, x, count = queue.popleft()

        if target_y == y and target_x == x:
            out = count

        # 상
        if y-1 >= 0 and maze_map[y-1][x] == 1:
            maze_map[y - 1][x] = 0
            queue.append((y - 1, x, count + 1))
        # 하
        if y+1 < len(maze_map) and maze_map[y+1][x] == 1:
            maze_map[y + 1][x] = 0
            queue.append((y + 1, x, count + 1))
        # 좌
        if x-1 >= 0 and maze_map[y][x-1] == 1:
            maze_map[y][x - 1] = 0
            queue.append((y, x-1, count + 1))
        # 우
        if x+1 < len(maze_map[0]) and maze_map[y][x+1] == 1:
            maze_map[y][x + 1] = 0
            queue.append((y, x+1, count + 1))

    return out

if __name__ == '__main__':
    n, m = map(int, input().split())

    maze_map = []
    for _ in range(n):
        maze_map.append(list(map(int, input())))

    print(solve_maze(maze_map, n-1, m-1))
