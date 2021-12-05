if __name__ == '__main__':
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    output = []

    for i in range(n):
        output.append(
            ''.join(list(
                map(lambda x: '#' if x == '1' else ' ', bin(arr1[i] | arr2[i])[2:]))
            )
        )

    print(output)