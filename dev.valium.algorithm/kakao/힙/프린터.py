import heapq
from collections import deque

def solution(priorities, location):
    arr = deque(list(map(lambda x: [x, False], priorities)))
    arr[location][1] = True
    priorities_heap = []
    for num in priorities:
        heapq.heappush(priorities_heap, (-num, num))

    output = 0
    while arr:
        cur = arr.popleft()

        if cur[0] == priorities_heap[0][1]:
            if cur[1]:
                return output + 1
            heapq.heappop(priorities_heap)[1]
            output += 1
        else:
            arr.append(cur)

    return output

if __name__ == '__main__':
    print(solution([1, 1, 9, 1, 1, 1] ,	0))