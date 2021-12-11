import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    output = 0
    while len(scoville) >= 2:

        if scoville[0] >= K:
            return output

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        modified = first + second * 2
        output += 1

        heapq.heappush(scoville, modified)

    if len(scoville) == 1:
        if scoville[0] >= K:
            return output
        else:
            return -1
    else:
        return -1

if __name__ == '__main__':
    print(solution([1] ,	7))