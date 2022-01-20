# TopologySort
큐/스택 알고리즘을 이용해 순서가 정해져있는 작업을 차례로 수행해야 할 때 
그 순서를 결정해주기 위해 사용하는 알고리즘

## 특징
* 사이클이 있는 그래프에서는 적용 할 수 없다.
> 거꾸로 사이클 판별로 사용 할 순 있지만, 그리디 알고리즘을 이용한 union 알고리즘이 존재한다.

## 흐름
1. 진입차수가 0인 정점을 큐에 삽입합니다. 
2. 큐에서 원소를 꺼내 연결된 모든 간선을 제거합니다.
3. 간선 제거 이후에 진입차수가 0이 된 정점을 큐에 삽입합니다.
4. 큐가 빌 때까지 2번 ~ 3번 과정을 반복합니다.

## 코드
```python
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
    # 1. 진입차수가 0인 정점을 큐에 삽입합니다. 
    for i in range(1, n + 1):
        if inDegreeCount[i] == 0:
            q.append(i)

    # 4. 큐가 빌 때까지 2번 ~ 3번 과정을 반복합니다.
    while q:
        curIndex = q.popleft()
        output.append(curIndex)

        # 2. 큐에서 원소를 꺼내 연결된 모든 간선을 제거합니다.
        for i in outDegree[curIndex]:
            inDegreeCount[i] -= 1

            # 3. 간선 제거 이후에 진입차수가 0이 된 정점을 큐에 삽입합니다.
            if inDegreeCount[i] == 0:
                q.append(i)
               
    # 큐가 비었지만 모든 간선이 제거 되지 않은경우 
    # sum(inDegreeCount) != 0: print("사이클이 존재합니다.")
    print(output)
```