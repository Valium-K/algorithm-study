from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    stack = deque([])
    time = 1
    stack_sum = 0
    while truck_weights:
        if bridge_length > len(stack) and stack_sum + truck_weights[0] <= weight:
            tw = truck_weights.popleft()
            stack.append((tw, bridge_length + time))
            stack_sum += tw
            time += 1
        else:
            w, t = stack.popleft()
            stack_sum -= w
            time = max(t, time)

        return stack[-1][1]
if __name__ == '__main__':
    print(solution(5,5 ,[1, 1, 1, 1, 1, 2, 2, 2, 2]), 19)
    print(solution(5 ,	5 ,	[2, 2, 2, 2, 1, 1, 1, 1, 1]), 19)
    print(solution(2, 10 ,[7 ,4 ,5 ,6]), 8)