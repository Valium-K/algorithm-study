import sys

sys.setrecursionlimit(15000)


def separate(p):
    adder = 0
    for i, char in enumerate(p):
        adder += 1 if char == '(' else -1
        if adder == 0:
            return (p[:i + 1], p[i + 1:])


def is_correct_string(u):
    if not u:
        return False
    if u[0] == ')':
        return False

    stack = [u[0]]
    for char in u[1:]:
        if not stack:
            if char == ')':
                return False
            stack.append(char)
        elif stack[-1] == char:
            stack.append(char)
        else:
            stack.pop()

    return True if not stack else False


def correct_string(u, v):
    return '(' + solution(v) + ')' + ''.join(list(map(lambda x: '(' if x == ')' else ')', (u[1:-1]))))


def solution(p):
    # 1
    if is_correct_string(p):
        return p
    if p == '':
        return p
    # 2
    u, v = separate(p)

    # 3, 4
    if is_correct_string(u):
        return u + solution(v)
    else:
        return correct_string(u, v)


if __name__ == '__main__':
    p = ''
    if not p:
        print('asdf')
