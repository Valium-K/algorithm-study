import math, itertools

def is_prime(num):
    if num == 2:
        return True

    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True
def solution(nums):
    return len(list(filter(lambda x: is_prime(x), map(sum, itertools.combinations(nums, 3)))))

if __name__ == '__main__':
    print(solution([1,2,3,4]))