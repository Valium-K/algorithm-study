'''
예시 test case는 통과 but 제출 시 '틀렸습니다'
'''
def get_area_of(game_map, cur_piece, cur_x, cur_y):
    output = 0

    for y, x in cur_piece:
        if cur_y + y >= len(game_map) or cur_x + x >= len(game_map[0]):
            return -1
        else:
            output += game_map[cur_y + y][cur_x + x]
    return output
def solve(game_map):
    # arr[종류][회전한조각들][0] = y좌표, arr[종류][회전][0] = x좌표
    arr = [
        # 1자
        [
            [(0, 0), (0, -1), (0, -2), (0, -3)],
            [(0, 0), (-1, 0), (-2, 0), (-3, 0)]
        ],
        # ㄴ자
        [
            [(-2, 0), (-1, 0), (0, 0), (0, 1)],
            [(1, 0), (0, 0), (0, 1), (0, 2)],
            [(0, -1), (0, 0), (1, 0), (2, 0)],
            [(-1, 0), (0, 0), (0, -1), (0, -2)],

            [(1, 0), (0, 0), (0, 1), (0, 2)],
            [(0, 0), (0, 1), (1, 0), (2, 0)],
            [(0, -2), (0, -1), (0, 0), (1, 0)],
            [(-2, 0), (-1, 0), (0, 0), (0, -1)]
        ],
        # ㅁ자
        [
            [(0, 0), (0, 1), (1, 0), (1, 1)]
        ],
        # ㄴㄱ자
        [
            [(0, 0), (1, 0), (1, 1), (2, 1)],
            [(0, 0), (1, 0), (1, -1), (0, 1)],
            [(0, 0), (1, 0), (0, 1), (-1, 1)],
            [(0, -1), (0, 0), (1, 0), (1, 1)]
        ],
        # ㅗ자
        [
            [(0, 0), (0, -1), (-1, 0), (1, 0)],
            [(0, 0), (0, -1), (-1, 0), (0, 1)],
            [(0, 0), (-1, 0), (1, 0), (0, 1)],
            [(0, 0), (0, -1), (0, 1), (1, 0)]
        ]
    ]
    output = 0
    for i in range(len(game_map)):
        for j in range(len(game_map[0])):

            for cur_pieces in arr:
                for cur_piece in cur_pieces:

                    cur_output = get_area_of(game_map, cur_piece, j, i)

                    if cur_output != -1 and cur_output > output:
                        output = cur_output
    return output
if __name__ == '__main__':
    n, m = map(int, input().split())
    game_map = [ list(map(int, input().split())) for _ in range(n) ]

    print(solve(game_map))