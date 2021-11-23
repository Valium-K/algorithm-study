n = int(input())
start_num = 1

while True:
    if start_num % n == 0:
        print(len(str(start_num)))
        break
    else:
        start_num = start_num * 10 + 1
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            start_num = 1

            while True:
                if start_num % n == 0:
                    print(len(str(start_num)))
                    break
                else:
                    start_num = start_num * 10 + 1
        except:
            break
