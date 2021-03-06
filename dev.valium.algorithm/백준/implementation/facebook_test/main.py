'''
๐ ๋ฌธ์ 

์ํ๋ฒณ ๋๋ฌธ์์ ์ซ์(0~9)๋ก๋ง ๊ตฌ์ฑ๋ ๋ฌธ์์ด์ด ์๋ ฅ์ผ๋ก ์ฃผ์ด์ง๋๋ค.
์ด๋ ๋ชจ๋  ์ํ๋ฒณ์ ์ค๋ฆ์ฐจ์์ผ๋ก ์ ๋ ฌํ์ฌ ์ด์ด์ ์ถ๋ ฅํ ๋ค์, ๊ทธ ๋ค์ ๋ชจ๋  ์ซ์๋ฅผ ๋ํ ๊ฐ์ ์ด์ด์ ์ถ๋ ฅํฉ๋๋ค.

์๋ฅผ ๋ค์ด K1KA5CB7 ์ด๋ผ๋ ๊ฐ์ด ๋ค์ด์ค๋ฉด ABCKK13์ ์ถ๋ ฅํฉ๋๋ค.

โ ์๋ ฅ ์กฐ๊ฑด
 -  ์ฒซ์งธ ์ค์ ํ๋์ ๋ฌธ์์ด S๊ฐ ์ฃผ์ด์ง๋๋ค. (1 <= S์ ๊ธธ์ด <= 10,000)

โ ์ถ๋ ฅ ์กฐ๊ฑด
 -  ์ฒซ์งธ ์ค์ ๋ฌธ์ ์์ ์๊ตฌํ๋ ์ ๋ต์ ์ถ๋ ฅํฉ๋๋ค.

์๋ ฅ ์์ 1
K1KA5CB7
์ถ๋ ฅ ์์ 1
ABCKK13

์๋ ฅ ์์ 2
AJKDLSI412K4JSJ9D
์ถ๋ ฅ ์์ 2
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

    # indicator == 0 -> ๋ฌธ์๋ก๋ง ๊ตฌ์ฑ
    # indicator+1 == len(str) -> ์ซ์๋ก๋ง ๊ตฌ์ฑ
    # 0 < indicator < len(str) -> ํผํฉ

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

    num = sum([int(x) for x in S if x.isdigit()]) # ์ํ๋ฒณ ์ ๋ ฌ
    alpha.sort()

    if num != 0:
        alpha.append(str(num))

    print(''.join(alpha))
if __name__ == '__main__':
    cool_solution()
    # my_solution()