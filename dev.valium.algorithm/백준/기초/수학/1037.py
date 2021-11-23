
if __name__ == '__main__':
    n = int(input())

    output = 0
    for i in range(1, n+1):
        output = output + (n // i) * i
    print(output)