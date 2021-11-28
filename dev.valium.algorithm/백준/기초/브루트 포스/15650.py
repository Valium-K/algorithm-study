def solve(n, m, cur, arr):

    for i in range(cur, n + 2):
        if len(arr) < m:
            solve(n, m, i + 1, arr + [i])
        else:
            for num in arr:
                print(num, end=' ')
            print()
            break

if __name__ == '__main__':
    n, m = map(int, input().split())


    solve(n, m, 1, [])