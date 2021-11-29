def is_suitable_forms(arr):
    mo = len(list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], arr)))
    za = len(arr) - mo

    if mo >= 1 and za >= 2:
        return True
    else:
        return False

def solve(l, c, arr, output):
    if sorted(output) != output:
        return

    if l == len(output):
        if is_suitable_forms(output):
            for i in output:
                print(i, end='')
            print()
        return

    for i in arr:
        if i not in output:
            solve(l, c, arr, output + [i])

if __name__ == '__main__':
    l, c = map(int, input().split())
    arr = sorted(list(input().split()))

    solve(l, c, arr, [])