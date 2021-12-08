def set_finger_pos(finger_pose, number):
    if number == 0:
        finger_pose[0] = 3
        finger_pose[1] = 1
    else:
        finger_pose[0] = (number - 1) // 3
        finger_pose[1] = (number - 1) % 3
def get_dist(finger_pos, number):
    target_pose = [-1, -1]
    set_finger_pos(target_pose, number)

    return abs(target_pose[0] - finger_pos[0]) + abs(target_pose[1] - finger_pos[1])
def solution(numbers, hand):
    answer = []
    left_finger_pos = [3, 0]
    right_finger_pos = [3, 2]
    hand = 'R' if hand == 'right' else 'L'

    for number in numbers:
        if number in [1, 4, 7]:
            answer.append('L')
            set_finger_pos(left_finger_pos, number)
        elif number in [3, 6, 9]:
            answer.append('R')
            set_finger_pos(right_finger_pos, number)
        else:
            left_dist = get_dist(left_finger_pos, number)
            right_dist = get_dist(right_finger_pos, number)
            
            if left_dist < right_dist:
                answer.append('L')
                set_finger_pos(left_finger_pos, number)
            elif left_dist > right_dist:
                answer.append('R')
                set_finger_pos(right_finger_pos, number)
            else:
                answer.append(hand)
                set_finger_pos(right_finger_pos if hand == 'R' else left_finger_pos, number)

    return ''.join(answer)

if __name__ == '__main__':
    print(solution([1,3,6,8,2], 'right'))