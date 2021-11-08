# k번 원소 수정을 통해 배열 1의 원소 총 합이 가장 크게 만드는 문제

if __name__ == '__main__':
    n, k = map(int, input().split())

    arr1 = sorted(list(map(int, input().split())))
    arr2 = sorted(list(map(int, input().split())), reverse=True)

    for i in range(k):
        if arr1[i] < arr2[i]:
            arr1[i] = arr2[i]
        else:
            break

    print(sum(arr1))
