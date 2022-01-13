# 24 18
# 6
# 72

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
def lcm(a, b, g):
    return int(a * b / g)
m, n = map(int, input().split())
g = gcd(m, n)
print(g)
print(lcm(m, n, g))
