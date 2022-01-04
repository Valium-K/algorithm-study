
def solution(number, k):
    output = ""
    targetLen = len(number) - k

    while True:
        if targetLen == 1:
            output += max(list(number))
            break
        if targetLen == len(number):
            output += number
            break

        cur = max(number[:-targetLen + 1])
        number = number[number.index(cur) + 1:]
        output += cur
        targetLen -= 1

    return output
if __name__ == '__main__':
    print(solution("4177252841" 	,4))