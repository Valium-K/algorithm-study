if __name__ == '__main__':
    n, k = map(int, input().split())

    cur = 1
    count = 0
    while n >= cur:
        if count == k:
            break

        if n % cur == 0:
            count += 1
        cur += 1

    if count == k:
        print(cur - 1)
    else:
        print(0)
