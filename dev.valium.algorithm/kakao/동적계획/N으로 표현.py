def solution(N, number):
    lst = [set() for _ in range(9)]
    lst[1].add(N)
    if N == number:
        return 1

    for i in range(2, 9):
        ni = int(str(N) * i)
        if ni == number:
            return i
        lst[i].add(ni)

        for j in range(1, i):
            for n in lst[j]:
                for m in lst[i - j]:
                    if n + m == number:
                        return i
                    lst[i].add(n + m)
                    if n - m == number:
                        return i
                    lst[i].add(n - m)
                    if n * m == number:
                        return i
                    lst[i].add(n * m)
                    if m != 0:
                        if n // m == number:
                            return i
                        lst[i].add(n // m)

    return -1
if __name__ == '__main__':
    print(solution(5, 12))