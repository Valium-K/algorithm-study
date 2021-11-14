'''
📌 문제

알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

예를 들어 K1KA5CB7 이라는 값이 들어오면 ABCKK13을 출력합니다.

✔ 입력 조건
 -  첫째 줄에 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 10,000)

✔ 출력 조건
 -  첫째 줄에 문제에서 요구하는 정답을 출력합니다.

입력 예시 1
K1KA5CB7
출력 예시 1
ABCKK13

입력 예시 2
AJKDLSI412K4JSJ9D
출력 예시 2
ADDIJJJKKLSS20
'''
from functools import reduce
def my_solution():
    input_str = sorted(list(input()))
    # A: 65, Z: 90 0: 48, 9: 57

    indicator = 0
    sum = 0
    for i in range(len(input_str)):
        if ord(input_str[i]) <= 57:
            sum += int(input_str[i])
        else:
            indicator = i
            break

    # indicator == 0 -> 문자로만 구성
    # indicator+1 == len(str) -> 숫자로만 구성
    # 0 < indicator < len(str) -> 혼합

    if indicator == 0:
        print(''.join(input_str))
    elif 0 < indicator < len(input_str):
        print(''.join(input_str[indicator:]), end='')
        print(sum)
    else:
        print(sum)

def cool_solution():
    S = input()
    # alpha = [x for x in S if x.isalpha()]
    alpha = list(filter(lambda x: x.isalpha(), S))

    num = sum([int(x) for x in S if x.isdigit()]) # 알파벳 정렬
    alpha.sort()

    if num != 0:
        alpha.append(str(num))

    print(''.join(alpha))
if __name__ == '__main__':
    cool_solution()
    # my_solution()