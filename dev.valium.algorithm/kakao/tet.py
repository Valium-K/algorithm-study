import heapq

def solution(n, times):
    desk_arr = [[0, time] for time in times]
    heapq.heapify(desk_arr)

    while n > 0:
        target_desk = desk_arr[0]

        for i in range(len(desk_arr)):
            if desk_arr[i][0] + desk_arr[i][1] < desk_arr[0][0] + desk_arr[0][1]:
                target_desk = desk_arr[i]

        target_desk[0] += target_desk[1]
        n -= 1
       # heapq.heapify(desk_arr)

    return max(desk[0] for desk in desk_arr)
if __name__ == '__main__':
    print(solution(6 ,	[7, 10]))