if __name__ == '__main__':
    arr = sorted([int(input()) for _ in range(9)])
    done = False

    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            two_sum = arr[i] + arr[j]

            if sum(arr) - two_sum == 100:
                for k in range(len(arr)):
                    if k != i and k != j:
                        print(arr[k])
                done = True
                break

        if done:
            break