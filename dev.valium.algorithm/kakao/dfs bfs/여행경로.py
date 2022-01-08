from collections import deque
output = []
def proc(cur, tickets, visited, waypoint):
    global output

    if False not in visited:
        return True

    for i, ticket in enumerate(tickets):
        if not visited[i] and ticket[0] == cur:
            visited[i] = True
            if proc(ticket[1], tickets, visited, waypoint + [cur]):
                output.append(waypoint + [cur] + [ticket[1]])
            visited[i] = False

    return False

def solution(tickets):
    proc("ICN", tickets, [False] * len(tickets), [])
    return sorted(output)[0]
if __name__ == '__main__':
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
