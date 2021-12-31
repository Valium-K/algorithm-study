from itertools import combinations
from collections import Counter
from functools import reduce

def solution(clothes):
    # output = 0
    # closet = Counter(map(lambda x: x[1], clothes))
    #
    # hit_rate, miss_rate = 0, 0
    # cache = dict()
    # for i in range(1, len(closet) + 1):
    #     for cloth_tuple in combinations(closet, i):
    #         if cloth_tuple[:-1] in cache:
    #             output = output + cache[cloth_tuple[:-1]] * closet[cloth_tuple[-1]]
    #
    #             hit_rate += 1
    #         else:
    #             cur = 1
    #             for cloth in cloth_tuple:
    #                 cur *= closet[cloth]
    #             cache[cloth_tuple] = cur
    #
    #             output += cur
    #
    #             miss_rate += 1
    #
    # print(hit_rate, miss_rate)
    #
    # return output

    return reduce(lambda a, c: a*c, map(lambda y: y[1] + 1, Counter(map(lambda x: x[1], clothes)).items()), 1) - 1

if __name__ == '__main__':
    solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"], ["crowmask123", "neck"],["crowmas12525k123", "neck"],
              ["crowm122ask123", "chest"], ["crowm1255ask123", "chest"], ["cr3wqwqqqowmask123", "foot"]])