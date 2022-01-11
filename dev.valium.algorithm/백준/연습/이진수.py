if __name__ == '__main__':
    for _ in range(int(input())):

        n = int(input())
        outputSet = set()
        binN = []
        while n >= 1:
            binN.append(n % 2)
            n = n // 2

        for i, b in enumerate(binN):
            if b == 1:
                outputSet.add(i)

        print(*sorted(list(outputSet)))
