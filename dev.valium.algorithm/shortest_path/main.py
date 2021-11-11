def normalization(alphabet):
    return ord(alphabet) - 97

if __name__ == "__main__":
    arr = [-1] * 26

    s = input()

    for i in range(len(s)):

        temp = normalization(s[i])
        if arr[temp] == -1:
            arr[temp] = i

    for i in range(len(arr)):
        print(arr[i], end=' ')