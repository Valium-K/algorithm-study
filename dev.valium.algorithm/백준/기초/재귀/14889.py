target_indexes = []
output = 123456789

def init_team_building(n, cur, depth, parent):
    # n 개 중 n/2개를 중복없이 and 순서 상관없이 뽑는 경우의 수

    if depth >= n // 2:
        target_indexes.append(parent)
        return

    for i in range(cur, n-1):
        init_team_building(n, i + 1, depth + 1, parent + [i])

def solve(s, n):
    global output

    for target in target_indexes:
        team_a = 0
        team_b = 0
        other_target = list(filter(lambda x: x not in target, [i for i in range(n)]))

        for i in target:
            for j in target:
                if i != j:
                    team_a += s[i][j]

        for i in other_target:
            for j in other_target:
                if i != j:
                    team_b += s[i][j]

        cur = abs(team_b - team_a)
        if output > cur:
            output = cur

if __name__ == '__main__':
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]

    init_team_building(n, 0, 0, [])
    solve(s, n)

    print(output)
