# input
# 2
# hong 95
# lee 77

# output
# [lee, hong]
if __name__ == '__main__':
    n = int(input())

    arr = []
    for _ in range(n):
        name, score = input().split()
        arr.append((name, int(score)))

    print(list(map(lambda ele: ele[0], sorted(arr,
                                              key=lambda key: key[1],
                                              reverse=True))))
