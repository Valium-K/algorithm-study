import math
if __name__ == '__main__':
    n = int(input())
    output = 0
    for i in map(int, input().split()):
        output += 1
        if i == 1:
            output -= 1
            continue
        for k in range(int(math.sqrt(i)), 1, -1):
            if i % k == 0:
                output -= 1
                break
    print(output)
