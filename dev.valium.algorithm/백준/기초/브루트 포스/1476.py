def spend_time(cur_time):
    if cur_time[0] + 1 > 15:
        cur_time[0] = 1
    else:
        cur_time[0] += 1
    if cur_time[1] + 1 > 28:
        cur_time[1] = 1
    else:
        cur_time[1] += 1

    if cur_time[2] + 1 > 19:
        cur_time[2] = 1
    else:
        cur_time[2] += 1

    return cur_time
if __name__ == '__main__':
    e, s, m = map(int, input().split())
    cur_time = [1, 1, 1]
    count = 1

    while True:
        if cur_time[0] == e and cur_time[1] == s and cur_time[2] == m:
            break

        spend_time(cur_time)
        count += 1
    print(count)