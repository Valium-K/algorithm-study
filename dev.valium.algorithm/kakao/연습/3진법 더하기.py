def solution(n):
    trinary = []

    while True:
        if 0 != 3 * (n // 3):
            trinary.append(n - 3*(n // 3))
            n = n // 3
        else:
            trinary.append(n - 3 * (n // 3))
            break

    answer = 0
    for i, cur_bit in enumerate(reversed(trinary)):
        answer += cur_bit * 3**i

    return answer
if __name__ == '__main__':
    print(solution(3))