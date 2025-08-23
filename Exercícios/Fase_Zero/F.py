import itertools

N = int(input())
while N not in range(4, 1001):
    N = int(input())

while True:
    A = list(input().split())
    for i in range(len(A)):
        A[i] = int(A[i])
    for elem in A:
        if elem not in range(-1000, 1001):
            continue
    if len(A) == N:
        break

Q = int(input())
while Q not in range(1, 4001):
    Q = int(input())

while True:
    q = [int(input()) for i in range(Q)]
    for elem in q:
        if elem not in range(-4000, 4001):
            continue
    break

for num in q:
    quantidade = 0
    for quadrupla in itertools.combinations(A, 4):
        if sum(quadrupla) == num:
            quantidade += 1
    print(quantidade)