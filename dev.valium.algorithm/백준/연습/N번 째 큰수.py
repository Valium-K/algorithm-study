if __name__ == '__main__':
    for arr in [ sorted(list(map(int, input().split())), reverse=True) for _ in range(int(input()))]:
        print(arr[2])