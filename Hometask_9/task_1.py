from random import randint

n = int(input('размер матрицы:\n'))
a = [[randint(-19, 19) for j in range(n)]
     for i in range(n)]
for row in a:
    print(*map('{:2d}'.format, row))

min_a = min(sum(a, []))
ind_min = sum(a, []).index(min_a) // len(a)

print('строка с миним элементом: ', ind_min + 1)
print(sum(a[ind_min]))
