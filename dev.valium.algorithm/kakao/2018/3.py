def next_index(stack, cur_index):
    if cur_index >= len(stack) - 1:
        return 0
    else:
        return cur_index + 1
def insert(stack, cur_index, city):
    stack[cur_index] = city

    return next_index(stack, cur_index)

if __name__ == '__main__':
    cache_size = int(input())
    cities = list(map(lambda x: str.lower(x), ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

    stack = ['none'] * cache_size
    output = 0
    cur_index = 0

    if cache_size <= 0:
        output = len(cities) * 5
        cities = []

    for city in cities:
        if city in stack:
            output += 1
        else:
            cur_index = insert(stack, cur_index, city)
            output += 5

    print(output)
