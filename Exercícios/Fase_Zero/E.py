import math

x = 1

Y, K = map(int, input('Y, K: ').split())

for i in range(K):
    x += math.gcd(x, Y)
    
print(x)