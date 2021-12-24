from collections import deque

def alpha_to_26nry(s):
    output = []
    arr = list(s)

    for c in arr:
        output.append(ord(c) - 65)

    return output
def fix_indicator(name):
    arr = deque(alpha_to_26nry(name))

    output = 0
    while True:
        if arr[0] == 0:
            arr.append(arr.popleft())
            output += 1
        else:
            break

    return arr, output
def get_min_change(n):
    if 26 - n < n:
        return 26 - n
    else:
        return n
def solution(name):

    arr, output = fix_indicator(name)
    zero_flag = False
    for i in arr:
        if i == 0:
            zero_flag = True
        output += get_min_change(i)

    padding = 0
    if zero_flag:
        padding_right = 0
        for i in range(1, len(arr)):
            if arr[i] == 0:
                padding_right += 1
            else:
                break

        padding_left = 0
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] == 0:
                padding_left += 1
            else:
                break

        if padding_right > padding_left:
            padding = len(arr) - padding_right - 1
        else:
            padding = len(arr) - padding_left - 1

        return output + padding
    else:
        return output + len(arr) - 1


if __name__ == '__main__':
    print(solution("ABAAAAAAAAABB"))