if __name__ == '__main__':
    n = int(input())
    arr1 = list(map(int, input().split()))
    stock = [0 for _ in range(max(arr1) + 1)]

    for i in range(n):
        stock[arr1[i]] += 1

    m = int(input())
    looking_for = list(map(int, input().split()))

    for i in range(m):
        if stock[looking_for[i]] > 0:
            print('yes', end=' ')
        else:
            print('no', end=' ')
