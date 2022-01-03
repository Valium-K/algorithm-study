def get_width_heights(num):
    output = []
    for h in range(1, (num // 2) + 2):
        w = (num // h)
        if w * h == num and w >= h:
            output.append((num // h, h))
    return output

def solution(brown, yellow):
    for y_w, y_h in get_width_heights(yellow):
        if y_w * 2 + y_h * 2 + 4 == brown:
            return [y_w+2, y_h+2]

if __name__ == '__main__':
    solution(24 	,24)