output = 0
def bfs(numbers, cur_index, cur_sum, target):
    global output

    if cur_index >= len(numbers):
        if cur_sum == target:
            output += 1
        return

    bfs(numbers, cur_index + 1, cur_sum + numbers[cur_index], target)
    bfs(numbers, cur_index + 1, cur_sum - numbers[cur_index], target)

def solution(numbers, target):
    global output

    bfs(numbers, 0, 0, target)
    return output
if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1] ,	3))