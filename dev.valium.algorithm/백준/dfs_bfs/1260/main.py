'''
https://www.acmicpc.net/problem/1260
'''

from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    for node in sorted(graph[start]):
        if not visited[node]:
            dfs(graph, node, visited)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    print(start, end=' ')

    while q:
        current_node = q.popleft()

        for going_to_visit_node in sorted(graph[current_node]):
            if not visited[going_to_visit_node]:
                visited[going_to_visit_node] = True
                q.append(going_to_visit_node)
                print(going_to_visit_node, end=' ')

if __name__ == '__main__':
    node, edge, start_node = map(int, input().split())

    visited = [False] * (node + 1)
    graph = [[] for _ in range(node + 1)]
    for _ in range(edge):
        node1, node2 = map(int, input().split())

        graph[node1].append(node2)
        graph[node2].append(node1)

    dfs(graph, start_node, visited)
    print()

    visited = [False] * (node + 1)
    bfs(graph, start_node, visited)
