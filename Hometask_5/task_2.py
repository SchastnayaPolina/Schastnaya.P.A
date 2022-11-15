n = int(input())
i = n
while i > 1:
    if n % i == 0:
        d = i
    i = i - 1
print(d)