# Kruskal
그리디 알고리즘과 Union 알고리즘을 이용한 최소 스패닝 트리 알고리즘.
최소 신장 트리와 그 가중치의 합을 구할 수 있다.

## 흐름
1. 그래프(weight, a, b)를 가중치 기준으로 오름차순 정렬
2. 사이클(union 알고리즘)이 아닌경우 해당(weight, a, b)를 선택 - 그리디 알고리즘

## 코드
``` python
# 방법 A =======================
def findParentA(parent, x):
    if parent[x] != x:
        x = findParentA(parent, parent[x])
    return parent[x]
    
def unionParent(parent, a, b):
    a = findParentA(parent, a)
    b = findParentA(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
# =============================  

# 방법 B =======================
def findNSetParent(parent, x):
    if parent[x] != x:
        parent[x] = findParentA(parent, parent[x])
    return parent[x]
# =============================

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
        # 방법 A
        if findParentA(parent, a) != findParentA(parent, b):
            unionParent(parent, a, b)
            
        # 방법 B
        # if findNSetParent(parent, a) != findNSetParent(parent, b):
        #     parent[findNSetParent(parent, a)] = findNSetParent(parent, b)

        result.append((a, b, weight))
        
    printResult(result)
```
