from itertools import combinations

def is_possible_dish(order, dish):
    # a b v f
    order_list = list(order)

    for d in dish:
        if d not in order_list:
            return False

    return True
def solution(orders, course):
    answer = []
    order_set = set()
    for order in orders:
        for dish in list(order):
            order_set.add(dish)

    for size in course:
        # ('A', 'C') ....

        comb_dishes = set()
        for order in orders:
            comb_dishes = comb_dishes.union(set(combinations(order, size)))
        # comb_dishes = list(combinations(order_set, size))

        # ('A', 'C')
        dish_stack = []
        for dish in comb_dishes:
            cur = 0
            for order in orders:

                if is_possible_dish(order, dish):
                    cur += 1

            if cur > 1:
                dish_stack.append([cur, dish])

        dish_stack.sort(key=lambda x: x[0], reverse=True)
        dish_nums = list(map(lambda x: x[0], dish_stack))
        target = 0 if dish_nums == [] else max(dish_nums)

        if target <= 1:
            continue

        if dish_nums.count(target) > 1:
            for dish in dish_stack:
                if dish[0] == target:
                    temp = ''.join(sorted(dish[1]))
                    if temp not in answer:
                        answer.append(temp)
                else:
                    break
        else:
            temp = ''.join(sorted(dish_stack[0][1]))
            if temp not in answer:
                answer.append(temp)

    answer.sort()
    return answer

if __name__ == '__main__':
    solution(["XYZ", "XWY", "WXA"] ,	[2,3,4])