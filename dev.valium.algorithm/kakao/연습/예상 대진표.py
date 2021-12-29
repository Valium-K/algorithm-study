def solution(n,a,b):
    target = (a - 1) ^ (b - 1)
    output = 0
    while True:
        if target:
            output += 1
            target = target >> 1
        else:
            return output