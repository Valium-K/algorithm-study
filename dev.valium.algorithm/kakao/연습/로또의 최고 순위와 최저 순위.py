def solution(lottos, win_nums):
    answer = []

    rank = 7
    for num in lottos:
        if num in win_nums:
            rank -= 1
    answer.append(min(6, rank - lottos.count(0)))
    answer.append(min(6, rank))

    return answer

if __name__ == '__main__':
    print(solution([44, 1, 2, 3, 314, 255]	, [31, 10, 45, 1, 6, 19]))