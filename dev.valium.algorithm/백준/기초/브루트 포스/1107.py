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
    for i in range(11):
        if i not in missing_nums:
            available_nums.append(i)

    given_nums = []
    for i in range(len(sliced_num)):
        lower = 0
        mid = 0
        higher = 0
        for k in range(1, 10):
            if circle_sub(sliced_num[i]) - k in available_nums:
                lower = circle_sub(sliced_num[i]) - k
                break

        if sliced_num[i] in available_nums:
            mid = sliced_num[i]

        for k in range(1, 10):
            if circle_plus(sliced_num[i]) + k in available_nums:
                higher = circle_plus(sliced_num[i]) + k
                break
        given_nums.append([lower, mid, higher])

    return given_nums
def get_close_num(num, given_nums):

    for l, m, h in given_nums[0]:
        get_close_jari_nums(num, )
def process(num, current_jaris):
    
if __name__ == '__main__':
    target = int(input())
    n = input()
    missing_nums = list(map(int, input().split()))

    print(get_close_num(target, missing_nums))
