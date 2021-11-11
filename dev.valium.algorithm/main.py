import copy

MAX_COUNT = 5
current_score = 0

def get_max_number(game_map):
    max_num = 0

    for i in range(len(game_map)):
        i_max_num = max(game_map[i])

        if max_num < i_max_num:
            max_num = i_max_num

    return max_num
def get_swiped_game_map(game_map, swipe):
    temp_map = copy.deepcopy(game_map)

    if swipe == "LEFT":
        for k in range(len(temp_map)):
            for i in range(len(temp_map) - 1):
                for j in range(i + 1, len(temp_map[0])):
                    if temp_map[k][i] == temp_map[k][j] or temp_map[k][i] == 0:
                        temp_map[k][i] += temp_map[k][j]
                        temp_map[k][j] = 0
                    else:
                        continue

    elif swipe == "RIGHT":
        for k in range(len(temp_map)):
            for i in range(len(temp_map) - 1, 0, -1):
                for j in range(i - 1, -1, -1):
                    if temp_map[k][i] == temp_map[k][j] or temp_map[k][i] == 0:
                        temp_map[k][i] += temp_map[k][j]
                        temp_map[k][j] = 0
                    else:
                        continue

    elif swipe == "UP":
        for k in range(len(temp_map)):
            for i in range(0, len(temp_map) - 1):
                for j in range(i + 1, len(temp_map[0])):
                    if temp_map[i][k] == temp_map[j][k] or temp_map[i][k] == 0:
                        temp_map[i][k] += temp_map[j][k]
                        temp_map[j][k] = 0
                    else:
                        break

    else:
        for k in range(len(temp_map)):
            for i in range(len(temp_map)-1, 0, -1):
                for j in range(i - 1, -1, -1):
                    if temp_map[i][k] == temp_map[j][k] or temp_map[i][k] == 0:
                        temp_map[i][k] += temp_map[j][k]
                        temp_map[j][k] = 0
                    else:
                        break

    return temp_map
def solve_game(game_map):
    global current_score

    solve(game_map, "UP", 1)
    solve(game_map, "DOWN", 1)
    solve(game_map, "LEFT", 1)
    solve(game_map, "DOWN", 1)

    return current_score
def solve(game_map, swipe, depth):
    global current_score; global MAX_COUNT

    if depth > MAX_COUNT:
        return

    max_number = get_max_number(game_map)
    if max_number > current_score:
        current_score = max_number
        return

    current_game_map = get_swiped_game_map(game_map, swipe)

    solve(current_game_map, "UP", depth + 1)
    solve(current_game_map, "DOWN", depth + 1)
    solve(current_game_map, "LEFT", depth + 1)
    solve(current_game_map, "RIGHT", depth + 1)

def printer(arr):
    for i in arr:
        print(i)
if __name__ == '__main__':
    # n = int(input())
    #
    # game_map = []
    # for _ in range(n):
    #     game_map.append(list(map(int, input().split())))

    # print(solve_game(game_map))

    arr = [
        [2, 2,2,2],
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2]
    ]
    arr2 = [
        [0,0,4,4],
        [0, 0, 4, 4],
        [0, 0, 4, 4],
        [0, 0, 4, 4]

    ]

    # printer(get_swiped_game_map(arr, "RIGHT"))
    # for _ in range(5):
    #     tempA = copy.deepcopy(get_swiped_game_map(arr, "RIGHT"))
    #     printer(tempA)
    #     print()


    tempB = copy.deepcopy(get_swiped_game_map(arr2, "RIGHT"))
    print()
    tc = get_swiped_game_map(tempB, "UP")
    printer(tc)
    print()
    printer(get_swiped_game_map(tc, "UP"))
    print(get_max_number(tc))