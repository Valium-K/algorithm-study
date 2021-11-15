'''
https://codeup.kr/problem.php?id=2605
'''
def find_where_to_touch(game_map, y, x, parent_color, depth):
    game_map[y][x] = 9

    # 상
    if y-1 >= 0 and game_map[y-1][x] == parent_color:
        depth = find_where_to_touch(game_map, y - 1, x, parent_color, depth + 1)
    # 하
    if y+1 < len(game_map) and game_map[y+1][x] == parent_color:
        depth = find_where_to_touch(game_map, y + 1, x, parent_color, depth + 1)
    # 좌
    if x-1 >= 0 and game_map[y][x-1] == parent_color:
        depth = find_where_to_touch(game_map, y, x-1, parent_color, depth + 1)
    # 우
    if x+1 < len(game_map[0]) and game_map[y][x+1] == parent_color:
        depth = find_where_to_touch(game_map, y, x+1, parent_color, depth + 1)
    # 사분면 다 막힌경우
    return depth

if __name__ == '__main__':

    game_map = []

    for _ in range(7):
        game_map.append(list(map(int, input().split())))

    output = 0
    for i in range(7):
        for j in range(7):
            if game_map[i][j] <= 5 and find_where_to_touch(game_map, i, j, game_map[i][j], 1) >= 3:
                output += 1

    print(output)