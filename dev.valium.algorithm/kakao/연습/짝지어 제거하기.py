if __name__ == '__main__':
    s = 'cdcd'
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if not stack:
        print(1)
    else:
        print(0)