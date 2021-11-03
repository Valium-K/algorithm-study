if __name__ == '__main__':
    steps = [[2, -1], [2, 1], [-2, -1], [-2, 1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    count = 0

    input_arr = input()
    row = ord(input_arr[0]) - 97
    col = int(input_arr[1]) - 1

    for i in range(8):
        if not (row + steps[i][0] < 0 or col + steps[i][1] < 0):
            count = count + 1

    print(count)