from functools import reduce

def get_YS(x):
    d = 2
    output_dict = {}
    while d <= x:
        if x % d == 0:
            try:
                output_dict[d] += 1
                x = x / d
            except Exception:
                x = x / d
                output_dict[d] = 1
        else:
            d = d + 1

    return reduce(lambda a, c: a * c, map(lambda x: x + 1, output_dict.values()), 1)
def solution(left, right):
    output = 0
    for num in range(left, right + 1):
        if get_YS(num) % 2 == 0:
            output += num
        else:
            output -= num

    return output
if __name__ == '__main__':
    print(solution(24, 27))