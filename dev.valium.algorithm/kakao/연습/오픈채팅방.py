def solution(record):
    user_dict = {}
    answer = []

    for s in record:
        cun = s.split()

        if cun[0] != 'Leave':
            user_dict[cun[1]] = cun[2]

    for s in record:
        cun = s.split()

        if cun[0] == 'Enter':
            answer.append(user_dict[cun[1]] + '님이 들어왔습니다.')
        elif cun[0] == 'Leave':
            answer.append(user_dict[cun[1]] + '님이 나갔습니다.')

    return answer