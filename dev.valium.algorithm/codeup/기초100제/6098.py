def is_able_to_go(ant_map, dir, y, x):
    try:
        if dir == 'right' and (ant_map[y][x+1] == 0 or ant_map[y][x+1] == 2):
            return True
        elif dir == 'down' and (ant_map[y+1][x] == 0 or ant_map[y+1][x] == 2):
            return True
        return False
    except:
        return False

def solve(ant_map, y, x):
    if ant_map[y][x] == 2:
        ant_map[y][x] = 9
        return
    ant_map[y][x] = 9

    if is_able_to_go(ant_map, 'right', y, x):
        solve(ant_map, y, x+1)
    elif is_able_to_go(ant_map, 'down', y, x):
        solve(ant_map, y+1, x)

if __name__ == '__main__':
    ant_map = [ list(map(int, input().split())) for _ in range(10) ]

    solve(ant_map, 1, 1)

    for i in ant_map:
        for j in i:
            print(j, end=' ')
        print()