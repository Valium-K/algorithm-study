'''
https://www.acmicpc.net/problem/18406
'''
def is_specific_condition(current_score):
    indicator = len(str(current_score)) // 2

    left_part_list = list(map(int, str(current_score)[:indicator]))
    right_part_list = list(map(int, str(current_score)[indicator:]))

    if sum(left_part_list) == sum(right_part_list):
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input())

    if is_specific_condition(n):
        print("LUCKY")
    else:
        print("READY")