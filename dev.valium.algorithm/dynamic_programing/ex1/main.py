output = 123456789

def make_one(x, depth):
    global output

    if x <= 1:
        if depth < output:
            output = depth
        return

    if x % 5 == 0:
        make_one(x // 5, depth + 1)
    if x % 3 == 0:
        make_one(x // 3, depth + 1)
    if x % 2 == 0:
        make_one(x // 2, depth + 1)

    make_one(x - 1, depth + 1)

if __name__ == '__main__':
    x = int(input())
    make_one(x, 0)
    print(output)