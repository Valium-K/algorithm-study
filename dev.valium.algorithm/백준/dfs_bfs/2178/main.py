'''
https://www.acmicpc.net/problem/2178
'''
from collections import deque

def solve_maze(maze_map, start_y, start_x):
    q = deque( [(start_y, start_x, -1)] )

    # 상 하 좌 우
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    maze_map[start_y][start_x] = -1

    while q:
        y, x, move_count = q.popleft()

        for dir_y, dir_x in dir:
            target_y = y + dir_y
            target_x = x + dir_x

            if 0 <= target_y < len(maze_map) and 0 <= target_x < len(maze_map[0]) and maze_map[target_y][target_x] == 1:
                q.append((target_y, target_x, move_count - 1))
                maze_map[target_y][target_x] = move_count - 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    maze_map = [ list(map(int, list(input()))) for i in range(n) ]

    solve_maze(maze_map, 0, 0)

    print(maze_map[n-1][m-1] * -1)