# 입력: 일반사과 x원, 청사과 x + 100원, 총 금액 1000원
# result: 가능한 [일반사과 개수, 청사과 개수] 만약 총 금액이 아니라면 -1 출력

def proc(cur, x, total, arr):
    if cur == total:
        print(arr)
        return
    if cur > total:
        return

    proc(cur + x, x, total, arr + [x])
    proc(cur + x + 3, x, total, arr + [x + 3])

def solution(x, total):
    proc(0, x, total, [])
if __name__ == '__main__':
    solution(10, 150)