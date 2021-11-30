output = 0

def set_max_pay(total_pay):
    global output

    if total_pay > output:
        output = total_pay

def solve(n, schedule, start_day, cur_pay):
    for cur_day in range(start_day, len(schedule)):
        target_day = cur_day + schedule[cur_day][0] - 1

        if target_day < len(schedule):
            if target_day + 1 >= len(schedule):
                set_max_pay(cur_pay + schedule[cur_day][1])
            else:
                solve(n, schedule, target_day + 1, cur_pay + schedule[cur_day][1])
        else:
            set_max_pay(cur_pay)

if __name__ == '__main__':
    n = int(input())
    schedule = []

    for _ in range(n):
        schedule.append(tuple(map(int, input().split())))

    solve(n-1, schedule, 0, 0)

    print(output)