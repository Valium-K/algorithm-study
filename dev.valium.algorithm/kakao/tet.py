from collections import Counter
import math
import time
from collections import deque
def gcd(a, b):
    if b == 0:
        print(a, b)
        return a
    else:
        print(a, b)
        return gcd(b, a % b)
if __name__ == '__main__':
    # 3
    # WatanabE
    # ITO
    # YamaMoto

    n = int(input())

    for _ in range(n):
        for c in input():
            if ord('A') <= ord(c) <= ord('Z'):
                print(chr(ord(c) + 32), end='')
            else:
                print(c, end='')
        print()