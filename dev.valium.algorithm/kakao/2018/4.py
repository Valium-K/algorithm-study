def to_time_format(time):
    return str(time // 3600).zfill(2) + ':' + str(time % 60).zfill(2)
def to_int(timetable):
    out_arr = []
    for time in timetable:
        sep = time.index(':')

        out_arr.append(int(time[:sep]) * 3600 + int(time[sep+1:]))
    return out_arr

if __name__ == '__main__':
    n = int(input())    # 1
    t = int(input())    # 1
    m = int(input())    # 5
    timetable = ['09:10', '09:09', '08:00']
    timetable = sorted(to_int(timetable))

    possible_timetable = [0] * m

    start = (n - 1) * m
    end = (n - 1) * m + m

    for i in range(len(timetable)):
        try:
            if start < end:
                possible_timetable[i] = timetable[i]
        except:
            continue
    start_time = 32400 + (n-1)*t
    print(possible_timetable)

    print(to_time_format(start_time))