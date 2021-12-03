cache = [0] * 1000

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)

    arr[2] = min(arr[2], arr[1]*2)

    for i in range(3, n+1):
        for j in range(1, i):
            temp = arr[j] * (i//j) + arr[i % j]
            arr[i] = min(arr[i], temp)

    print(arr[n])