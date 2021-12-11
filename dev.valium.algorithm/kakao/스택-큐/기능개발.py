def solution(progresses, speeds):
    answer = []

    cur_index = 0
    while cur_index < len(progresses):
        for i in range(cur_index, len(progresses)):
            progresses[i] += speeds[i]

        days = 0
        for i in range(cur_index, len(progresses)):
            if progresses[i] >= 100:
                cur_index += 1
                days += 1
            else:
                break

        if days > 0:
            answer.append(days)
    return answer

if __name__ == '__main__':
    print(solution([93, 30, 55], [1, 30, 5]))