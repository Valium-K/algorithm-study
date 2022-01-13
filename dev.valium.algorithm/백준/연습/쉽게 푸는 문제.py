import math
if __name__ == '__main__':
    n, m = map(int, input().split())
    gN = math.ceil((-1 + math.sqrt(1 + 8*(n-1))) / 2)
    hN = n-1 - ((gN-1) * ((gN-1) + 1)) / 2

    gM = math.ceil((-1 + math.sqrt(1 + 8*m)) / 2)
    hM = m - ((gM-1) * ((gM-1) + 1)) / 2

    N = ((gN-1) * ((gN-1) + 1) * (2 * (gN-1) + 1) / 6) + hN * gN
    M = ((gM-1) * ((gM-1) + 1) * (2 * (gM-1) + 1) / 6) + hM * gM

    print(int(M-N))