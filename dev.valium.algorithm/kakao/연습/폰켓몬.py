from itertools import combinations

def solution(nums):
    answer = len(nums) // 2
    pokemon_set = set(nums)

    if len(pokemon_set) >= answer:
        return answer
    else:
        return len(pokemon_set)

if __name__ == '__main__':
    print(solution([3,3,3,2,2,2] 	))