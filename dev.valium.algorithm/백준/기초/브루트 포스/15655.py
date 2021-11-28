def solve(n, m, arr, output, cur_index):
    if m == len(output):
        for i in output:
            print(i, end=' ')
        print()
        return

    for i in range(cur_index, len(arr)):
        solve(n, m, arr, output + [arr[i]], i + 1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())))

    solve(n, m, arr, [], 0)