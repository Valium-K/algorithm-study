import itertools

if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    permutations = list(itertools.permutations(arr, n))

    output = 0
    for i in range(len(permutations)):
        cur = 0
        for j in range(0, n - 1):
            cur += abs(permutations[i][j] - permutations[i][j + 1])
        if cur > output:
            output = cur

    print(output)