a = int(input())
b = int(input())
i = 0
while a != 0 and b != 0:
    if b > a:
        i = i + 1
        a = b
    else:
        a = b
    b = int(input())
print(i)