output = 0

def solve(n, possible_nums):
    global output

    if n <= 0:
        if n == 0:
            output += 1
        return

    for num in possible_nums:
        solve(n - num, possible_nums)

if __name__ == '__main__':
    possible_nums = [1, 2, 3]
    n = int(input())
    target_num = 0

    for _ in range(n):
        target_num = int(input())

        solve(target_num, possible_nums)
        print(output)
        output = 0
