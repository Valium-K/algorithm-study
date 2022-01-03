import heapq

def solution(operations):
    arr = []

    for op in operations:
        c, n = op.split()

        if c == 'I':
            heapq.heappush(arr, int(n))
        else:
            if arr and n == '-1':
                heapq.heappop(arr)
            elif arr and n == '1':
                arr.pop(arr.index(max(arr)))

    if not arr:
        return [0,0]
    else:
        return [max(arr), arr[0]]

    # arr = []
    # heapq.heappush(arr, 10)
    # heapq.heappush(arr, 5)
    # heapq.heappush(arr, 7)
    # heapq.heappush(arr, 1)
    # print(arr)


if __name__ == '__main__':
    solution(
  	["I 1","I 1", "I 1", "D 1", "D -1", "I 1"])