from random import randint as rd


def arrmax(arr):
    amax = arr[0][0]
    n = len(arr)
    for i in range(n):
        if max(arr[i]) > amax:
            amax = max(arr[i])
    return amax


def arrprint(a, b):
    for i in a:
        print(*i)
    print()
    for i in b:
        print(*i)
    print()


print('введите для первой матрицы количество строк : ')
na = int(input())
print('количество элементов в строке : ')
ma = int(input())
print('введите для второй матрицы количество строк : ')
nb = int(input())
print('количество элементов в строке : ')
mb = int(input())

a = [[rd(1, 50) for i in range(ma)] for j in range(na)]
b = [[rd(51, 100) for i in range(mb)] for j in range(nb)]

arrprint(a, b)

amax = arrmax(a)
bmax = arrmax(b)

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = bmax if a[i][j] == amax else a[i][j]
for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = amax if b[i][j] == bmax else b[i][j]

arrprint(a, b)