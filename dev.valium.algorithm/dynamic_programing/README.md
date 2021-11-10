# 바텀-업(상향)식 프로그래밍
`반복문`을 이용하여 작은 문제부터 풀어나가 큰 문제를 해결하는 방식.   
필요한 경우 `DP 테이블(캐싱)`을 사용해 연산 속도를 증가시킨다.

## 예제
```python
def fibo(num):
    cache = [0] * (num + 1)

    cache[1] = 1
    cache[2] = 1

    for i in range(3, num + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[num]

if __name__ == '__main__':
    print(fibo(10))

```
# 탑-다운(하향)식 프로그래밍
큰 문제를 해결하기위해 작은 문제를 호출하는 `재귀적` 방식.    
필요한 경우 `메모이제이션(캐싱)`을 사용해 한번 계산한 값을 저장해둔다

## 예제
```python
def fibo(num):
    cache = [0] * (num + 1)
    return fibo_proc(num, cache)

def fibo_proc(num, cache):
    if num <= 2:
        return 1

    if cache[num] == 0:
        cache[num] = fibo_proc(num - 1, cache) + fibo_proc(num - 2, cache)

    return cache[num]

if __name__ == '__main__':
    print(fibo(10))
```