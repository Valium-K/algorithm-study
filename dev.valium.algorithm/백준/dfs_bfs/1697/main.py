from collections import deque

cache = [123456789] * 100001

def solve(n, k):
    global cache

    if n == k:
        return 0
    if n > k:
        return n - k

    q = deque([(n, 0)])

    while cache[k] >= 123456789:
        cur_num, cur_depth = q.popleft()

        if 0 <= cur_num-1 <= 100000 and cache[cur_num - 1] == 123456789:
            cache[cur_num - 1] = cur_depth + 1
            q.append((cur_num - 1, cur_depth + 1))
        if 0 <= cur_num+1 <= 100000 and cache[cur_num + 1] == 123456789:
            cache[cur_num + 1] = cur_depth + 1
            q.append((cur_num + 1, cur_depth + 1))
        if 0 <= cur_num*2 <= 100000 and cache[cur_num * 2] == 123456789:
            cache[cur_num * 2] = cur_depth + 1
            q.append((cur_num * 2, cur_depth + 1))

    return cache[k]

if __name__ == '__main__':
    n, k = map(int, input().split())

    print(solve(n, k))