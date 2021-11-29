output = 0

def solve(n, schedule, start_day, cur_pay):
    global output

    for cur_day in range(start_day, len(schedule)):
        next_day = cur_day + schedule[cur_day][0]

        if next_day <= n+1 and next_day + schedule[next_day][0] <= n+1:
            solve(n, schedule, next_day, cur_pay + schedule[cur_day][1])
        else:
            total_pay = cur_pay + schedule[start_day][1]
            if total_pay > output:
                output = total_pay

if __name__ == '__main__':
    n = int(input())
    schedule = []

    for _ in range(n):
        schedule.append(tuple(map(int, input().split())))

    solve(n-1, schedule, 0, 0)

    print(output)