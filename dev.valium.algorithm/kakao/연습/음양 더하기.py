def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
        sum += absolutes[i] if signs[i] else -absolutes[i]

    return sum

if __name__ == '__main__':
    print(solution([4,4,7,12], [True,False,False,True]))
