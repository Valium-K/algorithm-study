# Kruskal
그리디 알고리즘과 Union 알고리즘을 이용한 최소 스패닝 트리 알고리즘.
최소 신장 트리와 그 가중치의 합을 구할 수 있다.

## 흐름
1. 그래프(weight, a, b)를 가중치 기준으로 오름차순 정렬
2. 사이클(union 알고리즘)이 아닌경우 해당(weight, a, b)를 선택 - 그리디 알고리즘

## 코드
``` python
def findParent(parent, x):
    # root 까지 부모를 따라 올라감
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

    # node index가 작은 node를 부모로 선택
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def printResult(result):
    print('최소 스패닝 트리:')
    for g in sorted(result):
        print(g)
    print('최소 스패닝 트리의 가중치 합:', sum(map(lambda x: x[2], result)))

if __name__ == '__main__':
    graph = []
    node, edge = map(int, input().split())
    for _ in range(edge):
        a, b, weight = map(int, input().split())
        graph.append((weight, a, b))
    graph.sort()

    # 초기 parent는 root와 같고 그것은 자기 자신이다.
    parent = [i for i in range(node + 1)]
    result = []
    for weight, a, b in graph:
        if findParent(parent, a) != findParent(parent, b):
            unionParent(parent, a, b)
            result.append((a, b, weight))

    printResult(result)
```
