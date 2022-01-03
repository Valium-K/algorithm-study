from collections import deque

def solution(prices):
    output = [0 for _ in range(len(prices))]
    q = deque([(prices[0], 0)])
    for i, price in enumerate(prices[1:]):
        while True:
            if q and q[0][0] > price:
                p, idx = q.popleft()
                output[idx] = i+1 - idx
            else:
                q.appendleft((price, i+1))
                break
    while True:
        if len(q) <= 1:
            break
        n, idx = q.pop()
        output[idx] = q[0][1] - idx

    return output


if __name__ == '__main__':
    print(solution([5, 1, 3, 2, 3]))