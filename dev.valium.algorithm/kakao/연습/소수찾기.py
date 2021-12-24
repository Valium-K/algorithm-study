from itertools import permutations
import math

def solution(numbers):
    arr = set()
    output = 0
    for i in range(1, len(numbers) + 1):
        arr = arr.union(set(map(int, set(map(lambda x: ''.join(x), permutations(list(numbers), i))))))


    for num in arr:
        if num < 2:
            continue
        if num == 2:
            output += 1
            continue

        is_prime = True
        for j in range(2, math.floor((math.sqrt(num))) + 1):
            if num % j == 0:
                is_prime = False
                break

        if is_prime:
            output += 1

    return output

if __name__ == '__main__':
    # print(solution("17"))
    print(math.sqrt(11))