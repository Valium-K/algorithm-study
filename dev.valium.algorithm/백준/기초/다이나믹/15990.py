if __name__ == '__main__':
    n = int(input())
    cache = [-1] * 100001

    cache[0] = 0
    cache[1] = 1
    cache[2] = 1
    cache[3] = 3
    for _ in range(n):
        k = int(input())
        if cache[k] == -1:
            for i in range(4, k+1):
                if cache[i] == -1:
                    cache[i] = cache[i-2] + cache[i-1]

            print(cache[k])
        else:
            print(cache[k])

