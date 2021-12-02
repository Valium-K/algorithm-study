def solve(n, arr):
    for i in range(n-1, 0, -1):
        if arr[i-1] < arr[i]:
            target_index = arr.index(sorted(list(filter(lambda x: x >= 0, map(lambda x: x - arr[i-1], arr[i:]))))[0] + arr[i-1])

            temp = arr[i-1]
            arr[i-1] = arr[target_index]
            arr[target_index] = temp

            for j in arr[:i]:
                print(j, end=' ')
            for j in sorted(arr[i:]):
                print(j, end=' ')

            return
    print(-1)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    solve(n, arr)

