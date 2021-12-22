from functools import cmp_to_key

def solution(numbers):
    return str(int(''.join(map(str, sorted(map(str, numbers), key=cmp_to_key(lambda a, b: 1 if int(a + b) < int(b + a) else -1))))))
if __name__ == '__main__':
    print(solution([0, 0, 0, 0]))