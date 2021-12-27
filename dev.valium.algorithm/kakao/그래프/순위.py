from collections import Counter

def solution(n, results):
    arr = [[0] * n for _ in range(n)]

    for result in results:
        arr[result[0] - 1][result[1] - 1] = 1

    output = []
    for i in range(n):
        temp = i
        rank = n
        while True:
            cur = sum(arr[temp])
            if cur > 1:
                rank = -1
                break
            elif cur == 1:
                rank -= 1
                temp = arr[temp].index(1)
            else:
                break

        if rank != -1:
            output.append(rank)

    print(output)
    return len(list(filter(lambda x: x == 1, Counter(output).values())))
    # return len(*Counter(output).most_common(1))

if __name__ == '__main__':
    print(solution(6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [2, 4], [2, 6]]), 6)