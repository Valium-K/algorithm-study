total_count = 123456789
cache = []

def count_coins(coins, target, depth):
    global total_count
    global cache

    if target == 0:
        total_count = depth
    if target < 0:
        return

    for i in coins:
        count_coins(coins, target - i, depth + 1)


if __name__ == '__main__':
    n, m = list(map(int , input().split()))

    coins = []
    for _ in range(n):
        coins.append(int(input()))

    cache = []
    count_coins(coins, m, 0)

    if total_count == 123456789:
        print(-1)
    else:
        print(total_count)