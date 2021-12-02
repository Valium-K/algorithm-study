def solve(n, arr):
    if len(arr) == n:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(n):
        if i+1 not in arr:
            solve(n, arr + [i+1])
if __name__ == '__main__':
    n = int(input())

    solve(n, [])