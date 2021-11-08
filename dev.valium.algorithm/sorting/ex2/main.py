# 단순 정렬 문제
if __name__ == '__main__':
    n = int(input())

    arr = []
    for _ in range(n):
        arr.append(int(input()))

    print(sorted(arr, reverse=True))
