import heapq

def solution(jobs):
    arr = []
    for i, job in enumerate(jobs):
        heapq.heappush(arr, [job[0] + job[1], i])

    cur = 0
    for job in arr:
        cur += abs(cur - job[0]) + job[1]

    print(cur // len(arr))
if __name__ == '__main__':
    solution([[0, 3], [1, 9], [2, 6]] 	)