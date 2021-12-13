def solution(answers):
    answer = [
        [1, 0],
        [2, 0],
        [3, 0]
    ]
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if std1[i % 5] == answers[i]:
            answer[0][1] += 1
        if std2[i % 8] == answers[i]:
            answer[1][1] += 1
        if std3[i % 10] == answers[i]:
            answer[2][1] += 1

    answer.sort(key=lambda x: (x[1], x[0]), reverse=True)

    max_value = answer[0][1]
    return list(reversed(list(map(lambda x: x[0], filter(lambda x: x[1] == max_value, answer)))))

if __name__ == '__main__':
    print(solution([1,3,2,4,2]))