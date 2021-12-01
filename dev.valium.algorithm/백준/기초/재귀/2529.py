output_arr = []

def solve(n, signs, cur_sign_index, nums, cur_num_index, visited, cur):
    global output_arr

    if cur_sign_index >= len(signs):
        output_arr.append(int(''.join(map(str, cur))))
        return

    if cur == []:
        for i in range(len(nums)):
            visited[i] = True
            solve(n, signs, cur_sign_index, nums, i, visited, cur + [i])
            visited[i] = False
        return

    sign = signs[cur_sign_index]

    if sign == '>':
        # 0 1 2 3 .. 중에서
        for i in range(len(nums)):
            # 방문해야하고 >을 만족하면
            if not visited[i] and nums[cur_num_index] > nums[i]:
                visited[i] = True
                solve(n, signs, cur_sign_index + 1, nums, i, visited, cur + [i])
                visited[i] = False
    else:
        for i in range(len(nums)):
            if not visited[i] and nums[cur_num_index] < nums[i]:
                visited[i] = True
                solve(n, signs, cur_sign_index + 1, nums, i, visited, cur + [i])
                visited[i] = False

if __name__ == '__main__':
    n = int(input())
    signs = list(input().split())
    nums = list(range(10))
    visited = [False] * 10

    solve(n, signs, 0, nums, 0, visited, [])

    print(max(output_arr))
    out_format = '%.' + str(len(signs) + 1) + 'd'
    print(out_format % min(output_arr))

