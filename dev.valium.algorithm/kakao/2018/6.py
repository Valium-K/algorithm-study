def mask_blocks(game_map, cur_icon, mask, y, x):
    temp_sum = 0

    for i in range(2):
        for j in range(2):
            try:
                if game_map[i+y][j+x] == cur_icon:
                    temp_sum += 1
                else:
                    raise Exception
            except Exception:
                return

    if temp_sum == 4:
        for i in range(2):
            for j in range(2):
                mask[i + y][j + x] = -1
def merge_map(game_map, mask):
    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            if mask[i][j] == -1:
                game_map[i][j] = -1
def remove_masked_blocks(game_map, mask):
    for i in range(len(game_map)-1, -1, -1):
        for j in range(len(game_map[0])-1, -1, -1):
            if mask[i][j] == -1:
                for k in range(i, -1, -1):
                    if mask[k][j] != -1:
                        mask[i][j] = mask[k][j]
                        mask[k][j] = -1
                        game_map[i][j] = game_map[k][j]
                        game_map[k][j] = -1

if __name__ == '__main__':
    m = int(input())
    n = int(input())
    output = 0
    game_map = [list(input()) for _ in range(m)]
    while True:
        mask = [[0] * n for _ in range(m)]
        for i in range(len(game_map)):
            for j in range(len(game_map[0])):
                if game_map[i][j] == -1:
                    continue
                mask_blocks(game_map, game_map[i][j], mask, i, j)
        if sum(mask, []).count(-1) == 0:
            break
        else:
            output += sum(mask, []).count(-1)
        merge_map(game_map, mask)
        remove_masked_blocks(game_map, mask)

    print(output)