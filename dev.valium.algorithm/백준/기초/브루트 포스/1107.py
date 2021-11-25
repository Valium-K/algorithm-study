'''
예시 test case는 통과 but 제출 시 '틀렸습니다'
'''
diff = 123456789
output = -1
def circle_sub(num):
    if num == 0:
        return 9
    else:
        return num - 1
def circle_plus(num):
    if num == 9:
        return 0
    else:
        return num + 1
def get_close_jari_nums(num, missing_nums):
    sliced_num = list(map(int, list(str(num))))

    available_nums = []
    for i in range(10):
        if i not in missing_nums:
            available_nums.append(i)

    given_nums = []
    for i in range(len(sliced_num)):
        lower = -1
        mid = -1
        higher = -1
        for k in range(0, 10):
            if circle_sub(sliced_num[i]) - k in available_nums:
                lower = circle_sub(sliced_num[i]) - k
                break

        if sliced_num[i] in available_nums:
            mid = sliced_num[i]

        for k in range(0, 10):
            if circle_plus(sliced_num[i]) + k in available_nums:
                higher = circle_plus(sliced_num[i]) + k
                break

        given_nums.append(list(filter(lambda x: x != -1, [lower, mid, higher])))

    return given_nums
def get_close_num(num, given_nums, cur_str, depth):
    global output
    global diff

    if len(cur_str) == len(str(num)):
        cur = abs(int(cur_str) - num)
        if cur < diff:
            output = int(cur_str)
            diff = cur
        return


    try:
        for i in range(len(given_nums[depth])):
            get_close_num(num, given_nums, cur_str + str(given_nums[depth][i]), depth + 1)
    except:
        return
def solve(num, missing_nums):
    given_nums = get_close_jari_nums(num, missing_nums)

    for i in range(len(given_nums[0])):
        get_close_num(num, given_nums, str(given_nums[0][i]), 1)

    if output == -1:
        return abs(100 - num)
    else:
        first_case = len(str(output)) + abs(num - output)
        second_case = abs(100 - num)

    return min(first_case, second_case)
if __name__ == '__main__':
    target = int(input())
    if int(input()) != 0:
        missing_nums = list(map(int, input().split()))
    else:
        missing_nums = []


    print(solve(target, missing_nums))
