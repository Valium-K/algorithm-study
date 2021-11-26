def solve(n, m, visited, arr):
    if len(arr) == m:
        for i in arr:
            print(i + 1, end=' ')
        print()
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            solve(n, m, visited, arr + [i])
            visited[i] = False

if __name__ == '__main__':
    n, m = map(int, input().split())

    visited = [False] * n
    arr = []

    solve(n, m, visited, arr)