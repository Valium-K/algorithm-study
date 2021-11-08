def cut_cake(cake, pivot_height):
    if cake - pivot_height > 0:
        return cake - pivot_height
    else:
        return 0

def cut_that_rice_cake(rice_cakes, target_sum, start, end):
    pivot_height = (start + end) // 2

    cut_cakes_sum = sum(list(map(lambda cake: cut_cake(cake, pivot_height), rice_cakes)))

    if cut_cakes_sum < target_sum:
        cut_that_rice_cake(rice_cakes, target_sum, start, pivot_height)
    elif target_sum < cut_cakes_sum:
        cut_that_rice_cake(rice_cakes, target_sum, pivot_height + 1, end)
    elif cut_cakes_sum == target_sum:
        print(pivot_height)
    else:
        print('나와선 안됨.')

if __name__ == '__main__':
    n, m = map(int, input().split())

    rice_cakes = list(map(int, input().split()))

    cut_that_rice_cake(rice_cakes, m, min(rice_cakes), max(rice_cakes))
