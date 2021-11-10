def ant(arr):
    output = 0

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if i - j != -1 and arr[i] + arr[j] > output:
                output = arr[i] + arr[j]

    print(output)

if __name__ == '__main__':
    # [1, 3, 1, 8]
    n = int(input())
    arr = list(map(int, input().split()))

    # ant(arr)

    cache = [0] * n

    cache[0] = arr[0]
    cache[1] = max(arr[0], arr[1])

    for i in range(2, n):
        cache[i] = max(cache[i - 1], cache[i - 2] + arr[i])

    print(cache[n - 1])
