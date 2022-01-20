from collections import deque

if __name__ == '__main__':
    n = 7
    inputArr = [
        [1, 2],
        [1, 5],
        [2, 3],
        [3, 4],
        [4, 6],
        [5, 6],
        [6, 7]
    ]

    outDegree = [[] for _ in range(n + 1)]
    inDegreeCount = [0] * (n + 1)
    for a, b in inputArr:
        outDegree[a].append(b)
        inDegreeCount[b] += 1

    output = []
    q = deque()
    for i in range(1, n + 1):
        if inDegreeCount[i] == 0:
            q.append(i)

    while q:
        curIndex = q.popleft()
        output.append(curIndex)

        for i in outDegree[curIndex]:
            inDegreeCount[i] -= 1

            if inDegreeCount[i] == 0:
                q.append(i)

    print(output)


