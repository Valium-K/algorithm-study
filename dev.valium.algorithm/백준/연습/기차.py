if __name__ == '__main__':
    cur = 0
    curMax = cur
    for _ in range(10):
        co, ci = map(int, input().split())
        cur = cur - co + ci
        curMax = max(cur, curMax)
    print(curMax)