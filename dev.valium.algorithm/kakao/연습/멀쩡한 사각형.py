def gcd(w, h):
    return w if h == 0 else gcd(h, w % h)
def solution(w, h):
    return w * h - (w + h - gcd(w, h))

if __name__ == '__main__':
    for i in range(1):
        w, h = 5, 3
        print(solution(w, h))
