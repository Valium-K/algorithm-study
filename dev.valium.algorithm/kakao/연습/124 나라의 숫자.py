def solution(n):

    output = []
    while n > 3:
        temp = 0
        if n % 3 == 0:
            temp = (n // 3) - 1
        else:
            temp = n // 3

        if n - temp * 3 == 3:
            output.append('4')
        elif n - temp * 3 == 0:
            output.append('1')
        else:
            output.append(str(n - temp * 3))

        n = temp

    if n == 3:
        output.append('4')
    elif n % 3 == 0:
        output.append('1')
    else:
        output.append(str(n))

    return ''.join(reversed(output))

if __name__ == '__main__':
    print(solution(10))

