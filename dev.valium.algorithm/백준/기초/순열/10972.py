output = []
flag = False

def solve(n, arr, depth, target):
    global output
    global flag

    if depth >= n:
        print(arr)
        return

    for i in range(n):
        if i+1 not in arr:
            solve(n, arr + [i+1], depth + 1, target)

if __name__ == '__main__':
    n = int(input())
    arr = [map(int, input().split())]

    solve(n, [], 0, arr)

