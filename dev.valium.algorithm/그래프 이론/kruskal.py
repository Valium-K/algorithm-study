def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

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

    result = []
    parent = [i for i in range(node + 1)]
    for weight, a, b in graph:
        if findParent(parent, a) != findParent(parent, b):
            # unionParent(parent, a, b)

            result.append((a, b, weight))

    printResult(result)