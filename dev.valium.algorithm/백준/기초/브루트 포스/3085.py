def solve(arr):
    max = 0
    # 가로 뒤집기
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            one = arr[i][j]
            an_other_one = arr[i][j+1]

            arr[i][j] = an_other_one
            arr[i][j+1] = one

            got_max = get_longest_row_or_col(arr)
            if got_max > max:
                max = got_max

            arr[i][j] = one
            arr[i][j+1] = an_other_one

    # 세로
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            one = arr[j][i]
            an_other_one = arr[j+1][i]

            arr[j][i] = an_other_one
            arr[j+1][i] = one

            got_max = get_longest_row_or_col(arr)
            if got_max > max:
                max = got_max

            arr[j][i] = one
            arr[j+1][i] = an_other_one

    return max
def get_longest_row_or_col(arr):
    max = 0
    cur_count = 1

    # 가로
    for i in range(len(arr)):
        cur_color = arr[i][0]
        cur_count = 1
        for j in range(1, len(arr[0])):
            if cur_color == arr[i][j]:
                cur_count += 1
            else:
                if cur_count > max:
                    max = cur_count
                cur_color = arr[i][j]
                cur_count = 1
        if cur_count > max:
            max = cur_count
    # 세로
    for i in range(len(arr)):
        cur_color = arr[0][i]
        cur_count = 1
        for j in range(1, len(arr[0])):
            if cur_color == arr[j][i]:
                cur_count += 1
            else:
                if cur_count > max:
                    max = cur_count
                cur_color = arr[j][i]
                cur_count = 1
        if cur_count > max:
            max = cur_count
    return max

if __name__ == '__main__':
    n = int(input())

    arr = [ list(input()) for _ in range(n) ]

    print(solve(arr))