def solution(N, stages):
    fail_rate = [[0, 0] for _ in range(N)]

    for stage in stages:
        for i in range(stage):
            if i != N:
                fail_rate[i][1] += 1
        if stage != N + 1:
            fail_rate[stage-1][0] += 1

    return list(map(lambda x: x[0],sorted(dict(zip([i+1 for i in range(len(fail_rate))],map(lambda x: 0 if x[1] == 0 else x[0] / x[1], fail_rate))).items(),key=lambda x: x[1], reverse=True)))


if __name__ == '__main__':
    print(solution(5 ,	[2, 1, 2, 6, 2, 4, 3, 3]))