from itertools import combinations
import re

def solution(orders, course):
    answer = []
    order_dict = dict()

    for i in range(len(orders)):
        orders[i] = ''.join(sorted(list(orders[i])))

    for order in orders:
        for char in order:
            try:
                order_dict[char] += 1
            except Exception:
                order_dict[char] = 1

    target_dishes = list(map(lambda x: x[0], sorted(order_dict.items(), key=lambda x: x[1], reverse=True)))

    output = 0
    output_str = ''

    for i in course:
        for cur in list(combinations(target_dishes, i)):

            cur_str = ''.join(sorted(cur))

            top = 0
            for order in orders:
                top += len(list(re.findall(cur_str, order)))

            if top > output:
                output = top
                output_str = cur_str

        answer.append(output_str)
        print(answer)
if __name__ == '__main__':
    solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])