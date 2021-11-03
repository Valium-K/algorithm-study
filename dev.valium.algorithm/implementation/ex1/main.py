if __name__ == '__main__':

    # 1백만 이하의 경우의 수는 완전 탐색으로 풀어도 된다.

    h = int(input())

    count = 0

    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1

    print(count)