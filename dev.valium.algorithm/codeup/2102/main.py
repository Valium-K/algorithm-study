'''
자연수 N이 입력될 때, 0과 1로 이루어진 N의 배수 중 가장 작은 자연수를 출력하시오.
'''
if __name__ == '__main__':
    MAX = 18446744073709551615
    start = 1

    n = int(input())

    while True:
        current_num = int(format(start, 'b'))
        if current_num >= MAX:
            start = 0
            break
        if current_num >= n and current_num % n == 0:
            break
        start += 1

    print(format(start, 'b'))